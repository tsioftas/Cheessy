from chess_board import Chessboard, Move
from utils import Coord
from common_imports import TODO_Type, Rook
from constants import Colour

import copy

"""
Class to be used for altering a chessboard.
"""
class ChessboardController(Chessboard):

  INITIAL_PIECES = [
      Rook(Coord(0, 0), Colour.White),
      Rook(Coord(7, 7), Colour.Black)
  ] # TODO: fill in!


  def __init__(self):
    pass

  def applyMove(self, chessboard: Chessboard, move: Move):
    chessboard._Chessboard__move_piece(move.piece, move.destination)