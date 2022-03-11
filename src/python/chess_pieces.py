from common_imports import List
from utils import Coord
from constants import _COLOUR

"""
Abstract parent class to represent a piece. 

Defines the shared among children properties...:
- pos (the position of the piece as a CoordType)
- chessboard (the Chessboard object where this piece is placed, may be None)

...and methods:
- get_destinations

"""
class PieceInterface:

    """
    position (utils.Coord): the position of the piece
    chessboard (chess_hardware.Chessboard): the chessboard where this piece 
    belongs, default is None.
    """
    def __init__(self, position: Coord, colour: _COLOUR):
        self.pos = position
        self.colour = colour
        self.name = "GenericPiece" # To be overwritten by concrete classes
        self.first_move_done = None
        self.moved_two_squares_in_last_turn = None

    
    """
    Returns a list with the possible destinations
    """
    def get_destinations(self):
        assert self.chessboard is not None, "Cannot get moves for a piece that is not on a board"
    
    def __str__(self):
        return f"{self.colour}_{self.name}@{self.pos}"
    
    def __repr__(self):
        return str(self)
    
def getPieceCopy(other: PieceInterface):
    t = type(other)
    if other.first_move_done is not None:
        if other.moved_two_squares_in_last_turn is not None:
            p = t(other.pos, other.colour, first_move_done=other.first_move_done)
            p.moved_two_squares_in_last_turn = other.moved_two_squares_in_last_turn
            return p
        else:
            return t(other.pos, other.colour, first_move_done=other.first_move_done)
    else:
        return t(other.pos, other.colour)

