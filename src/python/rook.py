from utils import Coord
from chess_pieces import PieceInterface
from constants import _COLOUR

class Rook(PieceInterface):

    def __init__(self,
        position: Coord,
        colour: _COLOUR,
        first_move_done: bool = False):
        super().__init__(position, colour)
        self.name = "Rook"
        self.first_move_done = first_move_done

