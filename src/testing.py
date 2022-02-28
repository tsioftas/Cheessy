from algorithm import Justinianus
from bishop import Bishop
from chess_board import Chessboard, Move
from constants import _COLOUR
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook
from utils import Coord


init_pieces = [Rook(Coord(0,0), _COLOUR.Black),
    Knight(Coord(0,1), _COLOUR.Black),
    Bishop(Coord(0,2), _COLOUR.Black),
    Queen(Coord(0,3), _COLOUR.Black),
    King(Coord(0,4), _COLOUR.Black),
    Bishop(Coord(0,5), _COLOUR.Black),
    Knight(Coord(2,5), _COLOUR.Black),
    Rook(Coord(0,7), _COLOUR.Black),
    Pawn(Coord(1,0), _COLOUR.Black),
    Pawn(Coord(1,1), _COLOUR.Black),
    Pawn(Coord(1,2), _COLOUR.Black),
    Pawn(Coord(1,3), _COLOUR.Black),
    Pawn(Coord(2,4), _COLOUR.Black),
    Pawn(Coord(1,5), _COLOUR.Black),
    Pawn(Coord(2,6), _COLOUR.Black),
    Pawn(Coord(1,7), _COLOUR.Black),

    Rook(Coord(6,0), _COLOUR.White),
    Knight(Coord(7,1), _COLOUR.White),
    Bishop(Coord(7,2), _COLOUR.White),
    Queen(Coord(7,3), _COLOUR.White),
    King(Coord(7,4), _COLOUR.White),
    Bishop(Coord(7,5), _COLOUR.White),
    Knight(Coord(7,6), _COLOUR.White),
    Rook(Coord(7,7), _COLOUR.White),
    Pawn(Coord(5,0), _COLOUR.White),
    Pawn(Coord(6,1), _COLOUR.White),
    Pawn(Coord(6,2), _COLOUR.White),
    Pawn(Coord(5,3), _COLOUR.White),
    Pawn(Coord(6,4), _COLOUR.White),
    Pawn(Coord(6,5), _COLOUR.White),
    Pawn(Coord(6,6), _COLOUR.White),
    Pawn(Coord(5,7), _COLOUR.White),
  ]

if __name__ == "__main__":
    algo = Justinianus(_COLOUR.Black, 2)
    algo.results_holder = Justinianus.BestResultHolder(algo.colour)
    chessboard = Chessboard(init_pieces)
    suspicious_bishop = chessboard.getPieces(_COLOUR.Black, Bishop)
    ma_bishop = suspicious_bishop[0]
    if ma_bishop.pos.y != 5:
        ma_bishop = suspicious_bishop[1]
    print(algo.get_next_move(chessboard))
    #print(algo.evaluate_move(1, Move(ma_bishop, Coord(5, 0)), chessboard))
    