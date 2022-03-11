import math
from typing import Callable
import numpy as np
from numpy.random import default_rng as defaultRng
import tensorflow as tf
from chessboard_data_manipulator import ChessboardDataManinpulator
from tensorflow.keras import datasets, layers, models, optimizers
import matplotlib.pyplot as plt

# Local imports
from chess_board import Chessboard
from chess_board_controller import ChessboardController, Move
from chess_pieces import PieceInterface
from common_imports import List, Dict, TODO_Type
from constants import _BOARD_X_DIM, _BOARD_Y_DIM, _COLOUR, \
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
from constants import _BOARD_X_DIM, _BOARD_Y_DIM
from queen import Queen
from rook import Rook
from bishop import Bishop
from utils import Coord

class SharedResources:
    
    def __init__(self):
        self.recursion_tree: au.RecursionTree = None
        self.current_state: au.RecursionTreeNode = None

class AlgorithmInterface:
    
    def __init__(self, colour: _COLOUR):
        self.colour = colour
        self.shared_resources = None

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
        if game_state == _GAME_STATES.CHECK:
            s += -cc*_JUSTINIANUS_CHECK_VALUE
        return s
    
    def justinianus_search_depth(moves):
        return 4
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
            # if self.colour == _COLOUR.White:
            #     sort_coef = -1
            # elif self.colour == _COLOUR.Black:
            #     sort_coef = 1
            # else:
            #     raise Exception("Cannot get move for player of unsupported/unknown colour: {self.colour}")
            # quickvalue_child_tuples: List[(float, au.RecursionTreeNode)] = [(Justinianus.simple_valfunction(n), n) for n in children]
            # quickvalue_child_tuples.sort(key=lambda x: sort_coef*x[0])
            # children = [c for _, c in quickvalue_child_tuples]
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
    
    def get_simple_valfunction(self):
        return Justinianus.simple_valfunction
    
    def create_recursion_tree(self, chessboard) -> au.RecursionTree:
        self.shared_resources.recursion_tree = au.RecursionTree()
        self.shared_resources.recursion_tree.initialize_tree(chessboard, 
            self.colour, 
            self.valfunction)
        self.shared_resources.current_state = self.shared_resources.recursion_tree.root
        return self.shared_resources.recursion_tree

    def get_next_move(self, chessboard: Chessboard) -> Move:
        # Useful stuff
        other_turn_colour = _OTHER_TURN_COLOUR[self.colour]
        # Deebugging stuff
        moves_options = OptionsDeterminerInterface.determine_options(self.colour, chessboard)
        number_of_moves = len(moves_options)
        print(f"Number of moves: {number_of_moves}")
        # Logic stuff
        # 2.Create search tree for this algorithm with current state as root
        if self.shared_resources.recursion_tree is None:
            rt = self.create_recursion_tree(chessboard)
        current_state = self.shared_resources.current_state
        current_state.expand()
        children = current_state.child_states
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

class Socrates(AlgorithmInterface):

    def __init__(self,
                 colour: _COLOUR):
        super().__init__(colour)
        self.colour = colour
    
    def get_next_move(self, chessboard: Chessboard) -> Move:
        options = OptionsDeterminerInterface.determine_options(self.colour, chessboard)
        while True:
            print(f"Select move for {self.colour} (x_from, y_from, x_to, y_to): ", end='')
            s = input()
            try:
                s = s.split(',')
                x_from = int(s[0])
                y_from = int(s[1])
                x_to = int(s[2])
                y_to = int(s[3])
                if len(s) == 5:
                    promotion_piece = s[4]
                else:
                    promotion_piece = None
                valid_coords =  0 <= x_from <= _BOARD_X_DIM-1 and 0 <= y_from <= _BOARD_Y_DIM \
                                and 0 <= x_to <= _BOARD_X_DIM-1 and 0 <= y_to <= _BOARD_Y_DIM
                promotion_ok = promotion_piece is None or promotion_piece in ["queen", "bishop", "rook", "knight"]
                if not promotion_piece is None:
                    promotion_type = {
                        "queen": Queen,
                        "bishop": Bishop,
                        "rook": Rook,
                        "knight": Knight
                    }[promotion_piece]
                else:
                    promotion_type = None
                if not valid_coords:
                    raise Exception("Invalid coordinates given, please try again.")
                if not promotion_ok:
                    raise Exception("Invalid promotion choice, please try again.")
                piece_to_move = chessboard.squares[x_from][y_from]
                valid_piece = piece_to_move is not None and piece_to_move.colour == self.colour
                if not valid_piece:
                    raise Exception("Invalid/ no piece selected, please try again.")
                for move in options:
                    if move.piece.pos.x == x_from and move.piece.pos.y == y_from \
                        and move.destination.x == x_to and move.destination.y == y_to:
                        if not promotion_piece is None and \
                            not move.promotion_piece is None and \
                                move.promotion_piece == promotion_type:
                            return move
                        elif promotion_piece is None and \
                            move.promotion_piece is None:
                            return move
                raise Exception("Invalid move selected.")
            except Exception as e:
                print(f"Error while parsing input: {e}")

class Pletho(AlgorithmInterface):

    def __init__(self,
                colour: _COLOUR,
                seed: int,
                data_manipulator: ChessboardDataManinpulator):
        super().__init__(colour)
        self.data_manipulator = data_manipulator
        data = self.data_manipulator.data
        self.N = data[0].shape[0]
        self.data_x = data[0].reshape((self.N, 8, 8, 1))
        self.data_y = data[1]
        self.colour = colour
        self.seed = seed
        self.rng = defaultRng(seed)
        self.cc = ChessboardController()
        self.model = self.get_model()

    
    def get_model(self):
        # Expected data encoding:
        # list of 64 integers:
        # .0-63: flattened board square contents:
        #   \ 0: empty square
        #   \ 1: white king
        #   \ 2: white queen
        #   \ 3: white rook
        #   \ 4: white knight
        #   \ 5: white bishop
        #   \ 6: white pawn
        #   \ 7-12: same order for black
        # Loss function will be a binary win/lose label, the final outcome of the game.
        self.batch_size = 128
        self.in_channels = 1
        self.in_kernel = (5,5)
        self.hidden_channels = 128
        self.hidden_kernel = self.in_kernel
        assert self.data_x.shape == (self.N, 8, 8, 1)

        model = models.Sequential()
        model.add(layers.Conv2D(self.in_channels, self.in_kernel, padding='same', strides=1, activation='relu', input_shape=(_BOARD_X_DIM, _BOARD_Y_DIM, 1)))
        model.add(layers.MaxPooling2D(pool_size=(2,2), padding='same'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(self.hidden_channels, self.hidden_kernel, padding='same', strides=1, activation='relu'))
        model.add(layers.MaxPooling2D(pool_size=(2,2), padding='same'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(self.hidden_channels, self.hidden_kernel, padding='same', strides=1, activation='relu'))
        model.add(layers.MaxPooling2D(pool_size=(2,2), padding='same'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(self.hidden_channels, self.hidden_kernel, padding='same', strides=1, activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(units=self.data_manipulator.n_metadata, activation='relu', use_bias=True))
        model.summary()
        model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
        model.fit(self.data_x, self.data_y, epochs=100, batch_size=32)
        return model
    
    def get_next_move(self, chessboard: Chessboard) -> Move:
        possible_moves = OptionsDeterminerInterface.determine_options(self.colour, chessboard)
        best_state_value = None
        best_moves = []
        for possible_move in possible_moves:
            resulting_chessboad = au.applyMoveToCopy(chessboard, possible_move)
            datum = self.data_manipulator.chessboard_to_datum(resulting_chessboad).reshape(1, chessboard.x_dim, chessboard.y_dim, 1)
            state_value  = self.model.predict(datum)[0][0] / (self.model.predict(datum)[0][0] + self.model.predict(datum)[0][1])
            if self.colour == _COLOUR.White:
                # wants to maximize value
                if best_state_value is None or state_value >= best_state_value:
                    if state_value == best_state_value:
                        best_moves.append(possible_move)
                    else:
                        best_state_value = state_value
                        best_moves = [possible_move]
            elif self.colour == _COLOUR.Black:
                # wants to minimize value
                if best_state_value is None or state_value < best_state_value:
                    if state_value == best_state_value:
                        best_moves.append(possible_move)
                    else:
                        best_state_value = state_value
                        best_moves = [possible_move]
        if len(best_moves) == 0:
            return None
        best_move = self.rng.choice(best_moves)
        if type(best_move) != Move:
            koupepi = 1
        return best_move


        