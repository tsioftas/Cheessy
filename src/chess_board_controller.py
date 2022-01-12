from bishop import Bishop
from chess_board import Chessboard, Move
from knight import Knight
from utils import Coord
from common_imports import TODO_Type, Rook
from constants import Colour
from pawn import Pawn

import copy

"""
Class to be used for altering a chessboard.
"""
class ChessboardController(Chessboard):

  INITIAL_PIECES = [
    Rook(Coord(0,0), Colour.Black),
    Knight(Coord(0,1), Colour.Black),
    Bishop(Coord(0,2), Colour.Black),
    # Black queen
    # Black king
    Bishop(Coord(0,5), Colour.Black),
    Knight(Coord(0,6), Colour.Black),
    Rook(Coord(0,7), Colour.Black),
    Pawn(Coord(1,0), Colour.Black),
    Pawn(Coord(1,1), Colour.Black),
    Pawn(Coord(1,2), Colour.Black),
    Pawn(Coord(1,3), Colour.Black),
    Pawn(Coord(1,4), Colour.Black),
    Pawn(Coord(1,5), Colour.Black),
    Pawn(Coord(1,6), Colour.Black),
    Pawn(Coord(1,7), Colour.Black),

    Rook(Coord(7,0), Colour.White),
    Knight(Coord(7,1), Colour.White),
    Bishop(Coord(7,2), Colour.White),
    # Black queen
    # Black king
    Bishop(Coord(7,5), Colour.White),
    Knight(Coord(7,6), Colour.White),
    Rook(Coord(7,7), Colour.White),
    Pawn(Coord(6,0), Colour.White),
    Pawn(Coord(6,1), Colour.White),
    Pawn(Coord(6,2), Colour.White),
    Pawn(Coord(6,3), Colour.White),
    Pawn(Coord(6,4), Colour.White),
    Pawn(Coord(6,5), Colour.White),
    Pawn(Coord(6,6), Colour.White),
    Pawn(Coord(6,7), Colour.White),
  ] # TODO: fill in!


  def __init__(self):
    pass

  def applyMove(self, chessboard: Chessboard, move: Move):
    chessboard._Chessboard__move_piece(move.piece, move.destination)