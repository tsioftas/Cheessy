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

  INITIAL_PIECES = [
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


  def __init__(self):
    pass

  def applyMove(self, chessboard: Chessboard, move: Move):
    if move is None:
      # No changes made
      return
    chessboard._Chessboard__move_piece(move.piece, move.destination)
    if move.replacement_piece is not None:
      # Used for pawn promotion
      chessboard._Chessboard__replace_piece(move.destination, move.replacement_piece)