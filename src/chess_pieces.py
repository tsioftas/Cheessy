from common_imports import List
from utils import Coord
from constants import Colour

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
    def __init__(self,
        position: Coord,
        colour: Colour):
        self.pos = position
        self.colour = colour
    
    """
    Returns a list with the possible destinations
    """
    def get_destinations(self):
        assert self.chessboard is not None, "Cannot get moves for a piece that is not on a board"

