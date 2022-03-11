# ifndef CONSTANTS_H
# define CONSTANTS_H

//**
 * @brief An enumeration for different player colours.
 *
 * Can be one of: BLACK, WHITE.
 */
enum Colour {
    BLACK, WHITE
};

//**
 * @brief An enumeration containing chess-terms one of which describes 
 * the current state.
 * 
 * Can be one of: NEUTRAL, CHECK, STALEMATE, CHECKMATE. States reserved for 
 * check and its variations are seen from the defender's POV
 */
enum GameStates {
    NEUTRAL, CHECK, STALEMATE, CHECKMATE
};

map<Colour, Colour>* _OTHER_TURN_COLOUR = nullptr;

/// Chessboard layout constants
const int _BOARD_X_DIM = 8;
const int _BOARD_Y_DIM = 8;

/// Justinianus algorithm constants
map<string, double>* _JUSTINIANUS_DEFAULT_PIECE_VALUE = nullptr;
const double _JUSTINIANUS_CHECKMATE_VALUE = 1000;
const double _JUSTINIANUS_STALEMATE_VALUE = 0.523;
const double _JUSTINIANUS_CHECK_VALUE = 1;
const double _JUSTINIANUS_THREAT_VALUE_COEFFICIENT = 0.5;

//**
 * @brief Initialize some constants which need to be initialized using code.
 *
 * MUST be called at the beginning of the program. 
 */
void initConstants();

# endif // CONSTANTS_H