from typing import Tuple
from common_imports import List
from constants import _BOARD_Y_DIM, _BOARD_X_DIM, _COLOUR
from chess_pieces import PieceInterface, getPieceCopy
from pawn import Pawn
from king import King
from queen import Queen
from knight import Knight
from bishop import Bishop
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

        self.x_dim: int = _BOARD_X_DIM
        self.y_dim: int = _BOARD_Y_DIM
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
        if type(piece) == Pawn or type(piece) == King or type(piece) == Rook:
            piece.first_move_done = True
        if not self.__is_empty_at(destination):
            assert self.__at(destination).colour != piece.colour, "Invalid move, cannot move to a square containing a piece of the same colour"
            # other piece is captured
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
    
    def getPieces(self, colour: _COLOUR, t: PieceInterface) -> List[PieceInterface]:
        ret = []
        for piece in self.pieces:
            if piece.colour == colour and type(piece) == t:
                ret.append(piece)
        return ret

    


"""
Used to represent potential moves (piece and destination).
"""
class Move:

    def __init__(self,
        piece: PieceInterface,
        destination: Coord,
        promotion_piece: PieceInterface = None,
        capture_piece: Pawn = None,
        castle: Tuple[Rook, Coord] = None):
            self.piece = piece
            self.destination = destination
            self.promotion_piece = promotion_piece
            self.capture_piece = capture_piece
            self.castle = castle
    
    def __str__(self):
        s = f"{self.piece} moves to {self.destination}. "
        if not self.capture_piece is None:
            s += f"{self.piece} captures {self.capture_piece} "
        if not self.promotion_piece is None:
            s += f"{self.piece} promoted {self.promotion_piece} "
        return s            
    
    def __repr__(self):
        return str(self)
    
    def to_chess_notation(self) -> str:
        promotion_piece_strs = {
            Queen: 'q',
            Rook: 'r',
            Bishop: 'b',
            Knight: 'n',
        }
        if self.promotion_piece is None:
            promotion_str = ""
        else:
            promotion_str = promotion_piece_strs[self.promotion_piece]
        return self.piece.pos.to_chess_notation() + self.destination.to_chess_notation() + promotion_str           

def getChessboardCopy(other: Chessboard):
    pieces_copy = [getPieceCopy(p) for p in other.pieces]
    return Chessboard(pieces_copy)

