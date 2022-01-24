import math
import numpy as np
from numpy.random import default_rng as defaultRng
from bishop import Bishop
# Local imports
from chess_board import Chessboard
from chess_board_controller import ChessboardController, Move
from chess_pieces import PieceInterface
from common_imports import List, Dict, TODO_Type
from constants import _COLOUR, _JUSITNIANUS_STOHASTIC_LIMIT, _JUSTINIANUS_PRUNE_COEFFICIENT, _JUSTINIANUS_PRUNE_LIMIT, _JUSTINIANUS_STOHASTIC_COEFFICIENT, \
    _OTHER_TURN_COLOUR, \
    _CHESS_TERMS, \
    _JUSTINIANUS_DEFAULT_PIECE_VALUE, \
    _JUSTINIANUS_SEARCH_DEPTH, \
    _JUSTINIANUS_SEARCH_REPETITIONS, \
    _JUSTINIANUS_CHECKMATE_VALUE, \
    _JUSTINIANUS_STALEMATE_VALUE
import algorithm_utils as au
from king import King
from knight import Knight
from options_determiner import OptionsDeterminerInterface
from pawn import Pawn
from queen import Queen
from rook import Rook
from utils import Coord

class AlgorithmInterface:
    
    def __init__(self, colour: _COLOUR):
        self.colour = colour

    def get_next_move(self,
        chessboard: Chessboard) -> Move:
        pass

class RandomAlgorithm(AlgorithmInterface):

    def __init__(self,
        colour: _COLOUR,
        seed: int):
        super().__init__(colour)
        self.rng = defaultRng(seed)
    
    def get_next_move(self, chessboard: Chessboard) -> Move:
        moves_options = OptionsDeterminerInterface.determine_options(self.colour, chessboard)
        if moves_options != []:
            return self.rng.choice(moves_options)
        else:
            return None

class Justinianus(AlgorithmInterface):

    class BestResultHolder:
        def __init__(self, colour_reference: _COLOUR):
            self.colour_reference: _COLOUR = colour_reference
            self.best_result: float = -_JUSTINIANUS_CHECKMATE_VALUE
            self.best_moves: List[Move] = []
        
        def update_if_better(self, move: Move, result: float):
            if math.isclose(self.best_result, result, abs_tol=1e-9):
                self.best_moves.append(move)
            elif result > self.best_result:
                print(f"[DEBUG] New best result: {result}")
                print(f"[DEBUG] Brought by move: {move}")
                self.best_moves = [move]
                self.best_result = result
            
        def get_best_result(self):
            return self.best_result

    def __init__(self,
        colour: _COLOUR,
        seed: int,
        piece_values: Dict[str, float] = {}):
        super().__init__(colour)
        self.rng = defaultRng(seed)
        if piece_values == {}:
            self.piece_values = _JUSTINIANUS_DEFAULT_PIECE_VALUE
        else:
            self.piece_values = piece_values
        self.cc = ChessboardController()
        self.running_test_best_result_holder = None
    
    def get_search_depth(moves):
        # how deep to make the search based on how many moves there are
        if moves >= 25:
            return 1
        if moves >= 20:
            return 1
        if moves >= 15:
            return 2
        if moves >= 10:
            return 3
        return 5
    
    def get_search_repetitions(moves):
        # how deep to make the search based on how many moves there are
        if moves >= 25:
            return 1
        if moves >= 20:
            return 1
        if moves >= 15:
            return 2
        if moves >= 10:
            return 2
        return 3
    
    def evaluate_move_base_case(self, move: Move, chessboard: Chessboard):
        player_colour: _COLOUR = move.piece.colour
        hypothetical_chessboard = au.applyMoveToCopy(chessboard, move)
        opponent_colour = _OTHER_TURN_COLOUR[player_colour]
        piece_value_coefficient = {
            player_colour: 1,
            opponent_colour: -1
        }
        move_type = au.getMoveType(move, chessboard)
        if move_type == _CHESS_TERMS.CHECKMATE:
            return _JUSTINIANUS_CHECKMATE_VALUE
        elif move_type == _CHESS_TERMS.STALEMATE:
            return _JUSTINIANUS_STALEMATE_VALUE
        s = 0
        for piece in hypothetical_chessboard.pieces:
            s += piece_value_coefficient[piece.colour] * self.piece_values[piece.name]
        # TODO: make this smarter?
        return s

    def evaluate_move(self, depth: int, move: Move, chessboard:Chessboard): 
        # Base case
        if depth == 0:
            return self.evaluate_move_base_case(move, chessboard)
        player_colour: _COLOUR = move.piece.colour
        opponent_colour: _COLOUR = _OTHER_TURN_COLOUR[player_colour]
        hypothetical_chessboard = au.applyMoveToCopy(chessboard, move)
        opponents_hypothetical_moves = OptionsDeterminerInterface.determine_options(opponent_colour, hypothetical_chessboard)
        opponents_values = []
        number_of_opponent_moves = len(opponents_hypothetical_moves)
        if number_of_opponent_moves > _JUSITNIANUS_STOHASTIC_LIMIT:
            # consider a random subset of possible moves to increase speed
            # i.e. stohastic move evaluation
            sample_size = math.floor(_JUSTINIANUS_STOHASTIC_COEFFICIENT * number_of_opponent_moves)
            opponents_hypothetical_moves = self.rng.choice(opponents_hypothetical_moves, size=sample_size, replace=False)
        piece_value_coefficient = {
            self.colour: 1,
            _OTHER_TURN_COLOUR[self.colour]: -1
        }
        running_best_value = -_JUSTINIANUS_CHECKMATE_VALUE
        global_best_value = self.results_holder.get_best_result() * piece_value_coefficient[opponent_colour] # change global best value sign depending on which player plays
        for i, opponents_hypothetical_move in enumerate(opponents_hypothetical_moves):
            opponents_value_of_move = self.evaluate_move(depth-1, opponents_hypothetical_move, hypothetical_chessboard)
            if opponents_value_of_move is None:
                hypothetical_move_type = au.getMoveType(opponents_hypothetical_move, hypothetical_chessboard)
                if hypothetical_move_type == _CHESS_TERMS.STALEMATE:
                    opponents_value_of_move = _JUSTINIANUS_STALEMATE_VALUE
                elif hypothetical_move_type == _CHESS_TERMS.CHECKMATE:
                    opponents_value_of_move = -_JUSTINIANUS_CHECKMATE_VALUE
                else:
                    raise AssertionError(f"Unexpected move type: {hypothetical_move_type}")
            opponents_values.append(opponents_value_of_move)
            if opponents_value_of_move > running_best_value:
                running_best_value = opponents_value_of_move
            if i > _JUSTINIANUS_PRUNE_LIMIT and running_best_value < global_best_value * _JUSTINIANUS_PRUNE_COEFFICIENT:
                # this sample doesn't seem to be doing so well. Prune the search
                break
        # Opponent would choose move with highest value
        opponents_value_of_resulting_state = running_best_value
        own_value_of_move = -opponents_value_of_resulting_state
        return own_value_of_move
        
    def get_next_move(self, chessboard: Chessboard) -> Move:
        
        other_turn_colour = _OTHER_TURN_COLOUR[self.colour]
        self.results_holder = Justinianus.BestResultHolder(self.colour)
        moves_options = OptionsDeterminerInterface.determine_options(self.colour, chessboard)
        
        target_print = 0
        print_step = 1
        number_of_moves_to_choose_from = len(moves_options)
        print(f"Number of moves to choose from: {number_of_moves_to_choose_from}")
        move_values: Dict[Move, float] = {} # map move to a value
        self.search_repetitions = Justinianus.get_search_repetitions(number_of_moves_to_choose_from)
        self.search_depth = Justinianus.get_search_depth(number_of_moves_to_choose_from)
        full_progress = self.search_repetitions * len(moves_options)
        progress = 0
        #move_values_list = []
        for _ in range(self.search_repetitions):
            for move in moves_options:
                if move not in move_values:
                    move_values[move] = 0
                move_value = self.evaluate_move(self.search_depth, move, chessboard)
                self.results_holder.update_if_better(move, move_value)
                move_values[move] += move_value
                progress += 1
                percent_complete = progress/full_progress*100
                if percent_complete >= target_print:
                    print(f"Progress: {percent_complete}%")
                    target_print += print_step
        move_evaluations = []
        for move in moves_options:
            move_value = move_values[move] / self.search_repetitions
            move_evaluations.append((move_value, move))
        move_evaluations.sort(key= lambda x: -x[0]) # descending value
        best_moves = []
        best_moves_value = move_evaluations[0][0]
        for move_value, move in move_evaluations:
            if not math.isclose(move_value, best_moves_value, abs_tol=1e-9):
                break
            best_moves.append(move)
        return self.rng.choice(best_moves)
