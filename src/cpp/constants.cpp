# include "constants.h"

void initConstants()
{
    // Other turn colour map
    _OTHER_TURN_COLOUR[Colour.WHITE] = Colour.BLACK;
    _OTHER_TURN_COLOUR[Colour.BLACK] = Colour.WHITE;
    // Justinianus stuff
    _JUSTINIANUS_DEFAULT_PIECE_VALUE["King"] = 100;
    _JUSTINIANUS_DEFAULT_PIECE_VALUE["Queen"] = 10;
    _JUSTINIANUS_DEFAULT_PIECE_VALUE["Rook"] = 6;
    _JUSTINIANUS_DEFAULT_PIECE_VALUE["Knight"] = 4;
    _JUSTINIANUS_DEFAULT_PIECE_VALUE["Bishop"] = 3;
    _JUSTINIANUS_DEFAULT_PIECE_VALUE["Pawn"] = 1;
}