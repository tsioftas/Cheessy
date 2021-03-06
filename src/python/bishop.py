from utils import Coord
from chess_pieces import PieceInterface
from constants import _COLOUR

class Bishop(PieceInterface):
    
    def __init__(self,
        position: Coord,
        colour: _COLOUR):
        super().__init__(position, colour)
        self.name = "Bishop"

