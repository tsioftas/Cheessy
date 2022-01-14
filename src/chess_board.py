from common_imports import List
from constants import BOARD_Y_DIM, BOARD_X_DIM, Colour
from chess_pieces import PieceInterface
from pawn import Pawn
from rook import Rook
from utils import Coord

"""
Describes an imaginary physical chessboard.
"""
class Chessboard:
        
    """
    Creates a new chessboard and initializes it as empty or, if provided,
    the given list of pieces and positions.

    pieces ([chess_pieces.PieceInterface]): A List of some rather anti-peace piece-objects that
                                   should be placed on the board.
    """
    def __init__(self,
     pieces: List[PieceInterface] = []):
        self.x_dim: int = BOARD_X_DIM
        self.y_dim: int = BOARD_Y_DIM
        # initialize squares as empty
        self.squares: List[List[PieceInterface]] = [[None for i in range(self.y_dim)] for j in range(self.x_dim)]
        # process any pieces given as arguments
        self.pieces = pieces
        for piece in self.pieces:
            pos = piece.pos
            self.squares[pos.x][pos.y] = piece
    
    def __is_empty_at(self, pos: Coord):
        return self.squares[pos.x][pos.y] is None

    def __at(self, pos: Coord):
        return self.squares[pos.x][pos.y]
    
    def __move_piece(self, piece: PieceInterface, destination: Coord):
        start = piece.pos
        if type(piece) == Pawn:
            piece.first_move_done = True
        if not self.__is_empty_at(destination):
            assert self.__at(destination).colour != piece.colour, "Invalid move, cannot move to a square containing a piece of the same colour"
            # other piece is captured
            # TODO: add capturing logic?
            captured_piece = self.__at(destination)
            self.pieces.remove(captured_piece)
        self.squares[start.x][start.y] = None
        self.squares[destination.x][destination.y] = piece
        piece.pos = destination
    
    def __replace_piece(self, position: Coord, replacement_type: PieceInterface):
        piece_to_remove = self.__at(position)
        replacement_piece = replacement_type(position, piece_to_remove.colour) # create instance
        self.pieces.remove(piece_to_remove)
        self.pieces.append(replacement_piece)
        self.squares[position.x][position.y] = replacement_piece


"""
Used to represent potential moves (piece and destination).
"""
class Move:

    def __init__(self,
        piece: PieceInterface,
        destination: Coord,
        replacement_piece: PieceInterface = None):
            self.piece = piece
            self.destination = destination
            self.replacement_piece = replacement_piece

