# ifndef PLAYER_H
# define PLAYER_H

# include "utils.h"
# include "algorithms.h"
# include "chessboard.h"
# include "pieces.h"

class Player
{
    Player(Colour colour, AlgorithmInterface algorithm /* TODO: add more! */);

    Move get_next_move(Chessboard chessboard);
};

class Move
{
    Move(PieceInterface piece, Coord destination);
};
# endif // PLAYER_H