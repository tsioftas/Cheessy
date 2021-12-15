import common_imports
from utils import Coord

"""
Abstract parent class to represent a piece. 

Defines the shared among children properties...:
- pos (the position of the piece as a CoordType)

...and methods:
- get_destinations

"""
class Piece:

    def __init__(self,
        position: Coord,
        board: Board):
        self.pos = position
    
    """
    Returns a list with the possible destinations
    """
    def get_destinations(self):
        pass
