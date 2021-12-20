from numpy.random import default_rng as defaultRng
# Local imports
from chess_board import Chessboard, Move
from chess_pieces import PieceInterface
from common_imports import List, Dict, TODO_Type
from constants import Colour
from options_determiner import OptionsDeterminerInterface

class AlgorithmInterface:
    
    def __init__(self, colour: Colour):
        self.colour = colour

    def get_next_move(self,
        chessboard: Chessboard) -> Move:
        # TODO: Add check-check
        pass

class RandomAlgorithm(AlgorithmInterface):

    def __init__(self,
        colour: Colour,
        seed: int):
        super().__init__(colour)
        self.rng = defaultRng(seed)
    
    def get_next_move(self, chessboard: Chessboard) -> Move:
        moves_options = OptionsDeterminerInterface.determine_options(self.colour, chessboard)
        if moves_options != []:
            return self.rng.choice(moves_options)
        else:
            return None
