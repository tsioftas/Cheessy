from utils import Coord
from chess_pieces import PieceInterface
from constants import _COLOUR

class Pawn(PieceInterface):
    
    def __init__(self,
        position: Coord,
        colour: _COLOUR,
        first_move_done : bool = False):
        super().__init__(position, colour)
        self.first_move_done = first_move_done
        self.moved_two_squares_in_last_turn = 0 # set to 1 by apply_move appropriately, determine options adds 1 if =1, otherwise sets to 0 
        self.name = "Pawn"

