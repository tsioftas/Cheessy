from bishop import Bishop
from chess_board import Chessboard, Move
from knight import Knight
from utils import Coord
from common_imports import TODO_Type
from constants import _COLOUR
from pawn import Pawn
from queen import Queen
from king import King
from rook import Rook

import copy

"""
Class to be used for altering a chessboard.
"""
class ChessboardController(Chessboard):

    DEFAULT_INITIAL_PIECES = [
    Rook(Coord(0,0), _COLOUR.Black),
    Knight(Coord(0,1), _COLOUR.Black),
    Bishop(Coord(0,2), _COLOUR.Black),
    Queen(Coord(0,3), _COLOUR.Black),
    King(Coord(0,4), _COLOUR.Black),
    Bishop(Coord(0,5), _COLOUR.Black),
    Knight(Coord(0,6), _COLOUR.Black),
    Rook(Coord(0,7), _COLOUR.Black),
    Pawn(Coord(1,0), _COLOUR.Black),
    Pawn(Coord(1,1), _COLOUR.Black),
    Pawn(Coord(1,2), _COLOUR.Black),
    Pawn(Coord(1,3), _COLOUR.Black),
    Pawn(Coord(1,4), _COLOUR.Black),
    Pawn(Coord(1,5), _COLOUR.Black),
    Pawn(Coord(1,6), _COLOUR.Black),
    Pawn(Coord(1,7), _COLOUR.Black),

    Rook(Coord(7,0), _COLOUR.White),
    Knight(Coord(7,1), _COLOUR.White),
    Bishop(Coord(7,2), _COLOUR.White),
    Queen(Coord(7,3), _COLOUR.White),
    King(Coord(7,4), _COLOUR.White),
    Bishop(Coord(7,5), _COLOUR.White),
    Knight(Coord(7,6), _COLOUR.White),
    Rook(Coord(7,7), _COLOUR.White),
    Pawn(Coord(6,0), _COLOUR.White),
    Pawn(Coord(6,1), _COLOUR.White),
    Pawn(Coord(6,2), _COLOUR.White),
    Pawn(Coord(6,3), _COLOUR.White),
    Pawn(Coord(6,4), _COLOUR.White),
    Pawn(Coord(6,5), _COLOUR.White),
    Pawn(Coord(6,6), _COLOUR.White),
    Pawn(Coord(6,7), _COLOUR.White),
    ]

    EASY_WIN = [
    King(Coord(7,7), _COLOUR.White),
    Rook(Coord(2,1), _COLOUR.White),
    Rook(Coord(3,1), _COLOUR.White),

    King(Coord(0,0), _COLOUR.Black),
    Rook(Coord(4,6), _COLOUR.Black),
    Rook(Coord(5,6), _COLOUR.Black)
    ]

    EN_PASSANT = [
        King(Coord(7,7), _COLOUR.White),
        Pawn(Coord(6,3), _COLOUR.White),

        King(Coord(0,0), _COLOUR.Black),
        Pawn(Coord(4,2), _COLOUR.Black)
    ]

    CASTLE = [
        King(Coord(7,4), _COLOUR.White),
        Rook(Coord(7,0), _COLOUR.White),
        Rook(Coord(7,7), _COLOUR.White),

        King(Coord(0,0), _COLOUR.Black)
    ]

    INITIAL_PIECES = DEFAULT_INITIAL_PIECES

    def __init__(self):
        pass

    def applyMove(self, chessboard: Chessboard, move: Move):
        if move is None:
            # No changes made
            return
        
        # reset variables that should be reset
        pawns = chessboard.getPieces(_COLOUR.White, Pawn)
        pawns.extend(chessboard.getPieces(_COLOUR.Black, Pawn))
        for pawn in pawns:
            pawn.moved_two_squares_in_last_turn = 0
        
        # special moves
        # en passant
        if type(move.piece) == Pawn:
            if abs(move.piece.pos.x - move.destination.x) == 2:
                move.piece.moved_two_squares_in_last_turn = 1

        if not move.capture_piece is None:
            # used for special captures (en passant)
            chessboard.pieces.remove(move.capture_piece)
        chessboard._Chessboard__move_piece(move.piece, move.destination)
        if move.promotion_piece is not None:
            # Used for pawn promotion
            chessboard._Chessboard__replace_piece(move.destination, move.promotion_piece)
        if move.castle is not None:
            chessboard._Chessboard__move_piece(move.castle[0], move.castle[1])
        
        