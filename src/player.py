from common_imports import TODO_Type
from chess_pieces import PieceInterface
from constants import _COLOUR
from utils import Coord
from chess_board import Chessboard
from algorithm import AlgorithmInterface

class Player:

    def __init__(self,
        colour: _COLOUR,
        algorithm: AlgorithmInterface,
        **kwargs):
        self.colour = colour
        self.algorithm = algorithm(colour, **kwargs)
    
    def get_next_move(self, chessboard: Chessboard):
        return self.algorithm.get_next_move(chessboard)
        

"""
Class to describe a move, i.e. a piece and its destination.
"""
class Move:

    def __init__(self,
        piece: PieceInterface,
        destination: Coord):
        self.piece = piece
        self.destination = destination