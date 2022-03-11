
from optparse import Option
from re import S
from shutil import move
from token import OP
from typing import Callable, List, Dict
import numpy as np

from chess_board import Chessboard

from chess_board_controller import ChessboardController, Move
from chess_board import Chessboard, Move, getChessboardCopy
from king import King
from options_determiner import OptionsDeterminerInterface
from constants import _COLOUR, _OTHER_TURN_COLOUR, _GAME_STATES, _WHITE_QUEEN_ASSET

__cc = ChessboardController()

class RecursionTree:

    # maps nodes to node information (to avoid re-calculations)
    __node_to_node_info_cache = {} 

    def __init__(self):
        self.root = None
    
    def initialize_tree(self,
        chessboard: Chessboard,
        initial_player: _COLOUR,
        valfunction: Callable[[Chessboard, int, int, _COLOUR], float]):
        self.chessboard = chessboard
        self.initial_player = initial_player
        self.root = RecursionTreeNode(chessboard, initial_player, valfunction, {}, parent=None)

class RecursionTreeNodeInformation:

    def __init__(self):
        self.game_state: _GAME_STATES = None
        self.depth_to_value: Dict[int, float] = {}

class RecursionTreeNode:

    def __init__(self,
        chessboard: Chessboard,
        current_player: _COLOUR,
        node_valfunction: Callable[[int, float, float], float],
        node_info_cache,
        parent=None):
        self.chessboard = chessboard
        self.current_player = current_player
        self.opponent = _OTHER_TURN_COLOUR[self.current_player]
        self.current_player_moves = OptionsDeterminerInterface.determine_options(current_player, chessboard)
        self.child_states: List[RecursionTreeNode] = None
        self.expanded = False
        self.parent = parent
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth+1
        self.node_valfunction = node_valfunction
        self.state_string = str(self.current_player)
        for piece in self.chessboard.pieces:
            self.state_string += str(piece)
        self.node_info_cache = node_info_cache
        self.node_info_cache[self] = RecursionTreeNodeInformation()
        self.node_info: RecursionTreeNodeInformation = self.node_info_cache[self]
    
    def __str__(self):
        return self.state_string
    
    def __hash__(self):
        return str.__hash__(str(self))

    def get_value(self, search_start_depth: int, alpha: float, beta: float) -> float:
        if not search_start_depth in self.node_info.depth_to_value:
            valfunction = self.node_valfunction
            self.node_info.depth_to_value[search_start_depth] = valfunction(self, alpha, beta, search_start_depth)
        return self.node_info.depth_to_value[search_start_depth]
    
    def get_game_state(self) -> _GAME_STATES:
        if self.node_info.game_state is None:
            self.node_info.game_state = self.get_chessboard_state()
        return self.node_info.game_state
    
    def get_chessboard_state(self) -> _GAME_STATES:
        if self.node_info.game_state is None:
            chessboard = self.chessboard
            current_player = self.current_player
            opponent = self.opponent
            # Is the player's king threatened?
            current_player_king_pos = chessboard.getPieces(current_player, King)[0].pos
            potential_moves = self.current_player_moves
            opponent_hypothetical_moves = OptionsDeterminerInterface.determine_options(opponent, chessboard, check_for_check=False)
            threatens_king = False
            for opponent_move in opponent_hypothetical_moves:
                threatens_king = threatens_king or current_player_king_pos.x == opponent_move.destination.x and current_player_king_pos.y == opponent_move.destination.y
                if threatens_king:
                    break
            if threatens_king:
                if len(potential_moves) == 0:
                    # no move is available
                    self.node_info.game_state = _GAME_STATES.CHECKMATE
                else:
                    self.node_info.game_state = _GAME_STATES.CHECK
            elif len(potential_moves) == 0:
                self.node_info.game_state = _GAME_STATES.STALEMATE
        return self.node_info.game_state
    
    def expand(self, chosen_move=None):
        if self.child_states is None or not chosen_move is None:
            if self.child_states is None:
                self.child_states = []
            self.child_to_move: Dict[RecursionTreeNode, Move] = {}
            self.move_to_child: Dict[Move, RecursionTreeNode] = {}
            moves_to_expand = self.current_player_moves if chosen_move is None else [chosen_move]
            for move in moves_to_expand:
                new_chessboard = applyMoveToCopy(self.chessboard, move)
                new_state = RecursionTreeNode(new_chessboard, self.opponent, self.node_valfunction, self.node_info_cache, self)
                self.child_states.append(new_state)
                self.child_to_move[new_state] = move
                enc_move = (move.piece.pos.x, move.piece.pos.y, move.destination.x, move.destination.y)
                self.move_to_child[enc_move] = new_state
        if not chosen_move is None:
            enc_move = (chosen_move.piece.pos.x, chosen_move.piece.pos.y, chosen_move.destination.x, chosen_move.destination.y)
            return self.move_to_child[enc_move]
    

def applyMoveToCopy(chessboard: Chessboard, move: Move) -> Chessboard:
    chessboard_copy = getChessboardCopy(chessboard)
    piece_copy = chessboard_copy.squares[move.piece.pos.x][move.piece.pos.y]
    if not move.capture_piece is None:
        capture_piece_copy = chessboard_copy.squares[move.capture_piece.pos.x][move.capture_piece.pos.y]
    else:
        capture_piece_copy = None
    if move.castle is not None:
        castle_copy = (chessboard_copy.squares[move.castle[0].pos.x][move.castle[0].pos.y], move.castle[1])
    else:
        castle_copy = None
    move_copy = Move(piece_copy, move.destination, move.promotion_piece, capture_piece_copy, castle_copy)
    __cc.applyMove(chessboard_copy, move_copy)
    return chessboard_copy
    


    
        