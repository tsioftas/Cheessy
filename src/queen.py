from utils import Coord
from chess_pieces import PieceInterface
from constants import Colour

class Queen(PieceInterface):
    
    def __init__(self,
        position: Coord,
        colour: Colour):
        super().__init__(position, colour)
        self.name = "Queen"
