import math
from typing import Callable
import numpy as np
from numpy.random import default_rng as defaultRng
from bishop import Bishop
# Local imports
from chess_board import Chessboard
from chess_board_controller import ChessboardController, Move
from chess_pieces import PieceInterface
from common_imports import List, Dict, TODO_Type
from constants import _COLOUR, \
    _OTHER_TURN_COLOUR, \
    _GAME_STATES, \
    _JUSTINIANUS_DEFAULT_PIECE_VALUE, \
    _JUSTINIANUS_CHECKMATE_VALUE, \
    _JUSTINIANUS_STALEMATE_VALUE, \
    _JUSTINIANUS_CHECK_VALUE, \
    _JUSTINIANUS_THREAT_VALUE_COEFFICIENT
import algorithm_utils as au
from king import King
from knight import Knight
from options_determiner import OptionsDeterminerInterface
from pawn import Pawn
from queen import Queen
from rook import Rook
from utils import Coord

class SharedResources:
    
    def __init__(self):
        self.recursion_tree: au.RecursionTree = None
        self.current_state: au.RecursionTreeNode = None

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

    def __init__(self,
        colour: _COLOUR,
        seed: int,
        shared_resources: SharedResources,
        piece_values: Dict[str, float] = {}):
        super().__init__(colour)
        self.rng = defaultRng(seed)
        if piece_values == {}:
            self.piece_values = _JUSTINIANUS_DEFAULT_PIECE_VALUE
        else:
            self.piece_values = piece_values
        self.cc = ChessboardController()
        self.running_test_best_result_holder = None
        self.shared_resources = shared_resources

    def simple_valfunction(node: au.RecursionTreeNode):
        game_state = node.get_chessboard_state()
        colour_coefficients = {
            _COLOUR.White: 1,
            _COLOUR.Black: -1
        }
        cc = colour_coefficients[node.current_player]
        if game_state == _GAME_STATES.CHECKMATE:
            return -cc*_JUSTINIANUS_CHECKMATE_VALUE
        elif game_state == _GAME_STATES.STALEMATE:
            return -cc*_JUSTINIANUS_STALEMATE_VALUE
        s = 0
        for piece in node.chessboard.pieces:
            s += colour_coefficients[piece.colour] * _JUSTINIANUS_DEFAULT_PIECE_VALUE[piece.name]
        for colour in [_COLOUR.White, _COLOUR.Black]:
            player_options = OptionsDeterminerInterface.determine_options(colour, node.chessboard, True)
            for move in player_options:
                target_piece = node.chessboard.squares[move.destination.x][move.destination.y]
                if not target_piece is None:
                    # target piece is threatened 
                    s += colour_coefficients[piece.colour] * _JUSTINIANUS_THREAT_VALUE_COEFFICIENT * _JUSTINIANUS_DEFAULT_PIECE_VALUE[target_piece.name]
        if game_state == _GAME_STATES.CHECK:
            s += -cc*_JUSTINIANUS_CHECK_VALUE
        return s
    
    def justinianus_search_depth(moves):
        if moves >= 15:
            return 3
        elif moves >= 10:
            return 4
        elif moves >= 5:
            return 5
        return 6
    
    def valfunction(self, node: au.RecursionTreeNode, alpha: float, beta: float, search_start_depth: int):
        depth = node.depth
        max_depth = search_start_depth + Justinianus.justinianus_search_depth(self.number_of_moves)
        current_player = node.current_player
        assert depth <= max_depth, f"Invalid node depth: {depth} is deeper than maximum depth (which is {max_depth}"
        if depth  == max_depth:
            return Justinianus.simple_valfunction(node)
        else:
            node.expand()
            children = node.child_states
            if self.colour == _COLOUR.White:
                sort_coef = -1
            elif self.colour == _COLOUR.Black:
                sort_coef = 1
            else:
                raise Exception("Cannot get move for player of unsupported/unknown colour: {self.colour}")
            quickvalue_child_tuples: List[(float, au.RecursionTreeNode)] = [(Justinianus.simple_valfunction(n), n) for n in children]
            quickvalue_child_tuples.sort(key=lambda x: sort_coef*x[0])
            children = [c for _, c in quickvalue_child_tuples]
            if current_player == _COLOUR.White:
                value = -_JUSTINIANUS_CHECKMATE_VALUE
                for child in children:
                    value = max(value, child.get_value(search_start_depth, alpha=alpha, beta=beta))
                    if value >= beta:
                        break
                    alpha = max(alpha, value)
            elif current_player == _COLOUR.Black:
                value = _JUSTINIANUS_CHECKMATE_VALUE
                for child in children:
                    value = min(value, child.get_value(search_start_depth, alpha=alpha, beta=beta))
                    if value <= alpha:
                        break
                    beta = min(beta, value)
            else:
                raise Exception(f"Unexpected player colour: {current_player}")
            return value
    
    def get_next_move(self, chessboard: Chessboard) -> Move:
        # Useful stuff
        other_turn_colour = _OTHER_TURN_COLOUR[self.colour]
        # Deebugging stuff
        moves_options = OptionsDeterminerInterface.determine_options(other_turn_colour, chessboard)
        number_of_moves = len(moves_options)
        print(f"Number of moves: {number_of_moves}")
        # Logic stuff
        # 2.Create search tree for this algorithm with current state as root
        if self.shared_resources.recursion_tree is None:
            self.shared_resources.recursion_tree = au.RecursionTree()
            self.shared_resources.recursion_tree.initialize_tree(chessboard, 
                self.colour, 
                self.valfunction)
            self.shared_resources.current_state = self.shared_resources.recursion_tree.root
        current_state = self.shared_resources.current_state
        current_state.expand()
        children = current_state.child_states
        if self.colour == _COLOUR.White:
            sort_coef = -1
        elif self.colour == _COLOUR.Black:
            sort_coef = 1
        else:
            raise Exception("Cannot get move for player of unsupported/unknown colour: {self.colour}")
        quickvalue_child_tuples: List[(float, au.RecursionTreeNode)] = [(Justinianus.simple_valfunction(n), n) for n in children]
        quickvalue_child_tuples.sort(key=lambda x: sort_coef*x[0])
        children = [c for _, c in quickvalue_child_tuples]
        value_child_tuples: List[(float, au.RecursionTreeNode)] = []
        self.number_of_moves = len(children)
        alpha = -_JUSTINIANUS_CHECKMATE_VALUE
        beta = _JUSTINIANUS_CHECKMATE_VALUE
        for i, child in enumerate(children):
            progress = i / len(children) * 100
            print(f"Progress: {progress}%")
            child_value = child.get_value(current_state.depth, alpha, beta)
            value_child_tuples.append((child_value, child))
        value_child_tuples.sort(key=lambda x: x[0])
        if self.colour == _COLOUR.White:
            best_choice: au.RecursionTreeNode = value_child_tuples[-1][1]
        elif self.colour == _COLOUR.Black:
            best_choice: au.RecursionTreeNode = value_child_tuples[0][1]
        else:
            raise Exception(f"Cannot choose best move for unknown player: {self.colour}")
        best_move = current_state.child_to_move[best_choice]
        # TODO: might want to move the following line somewhere else (not really part of the algorithm to do this job)
        self.shared_resources.current_state = best_choice
        return best_move


