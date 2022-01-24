import enum

_COLOUR = enum.Enum("Colours", "Black White")
_CHESS_TERMS = enum.Enum("Chess_terms", "STALEMATE CHECKMATE")
_OTHER_TURN_COLOUR = {
            _COLOUR.White: _COLOUR.Black,
            _COLOUR.Black: _COLOUR.White
    }


# Chessboard layout constants
_BOARD_Y_DIM = 8
_BOARD_X_DIM = 8

# Graphics-related constants
_DISPLAY_HEIGHT = 800
_DISPLAY_WIDTH = 600
_ASSETS_PATH = "assets"
_BLACK_SQUARE_ASSET = "black_square.png"
_WHITE_SQUARE_ASSET = "white_square.png"
_BLACK_ROOK_ASSET = "black_rook.png"
_WHITE_ROOK_ASSET = "white_rook.png"
_BLACK_KNIGHT_ASSET = "black_knight.png"
_WHITE_KNIGHT_ASSET = "white_knight.png"
_BLACK_BISHOP_ASSET = "black_bishop.png"
_WHITE_BISHOP_ASSET = "white_bishop.png"
_BLACK_PAWN_ASSET = "black_pawn.png"
_WHITE_PAWN_ASSET = "white_pawn.png"
_BLACK_QUEEN_ASSET = "black_queen.png"
_WHITE_QUEEN_ASSET = "white_queen.png"
_BLACK_KING_ASSET = "black_king.png"
_WHITE_KING_ASSET = "white_king.png"



# Justinianus algorithm constants
_JUSTINIANUS_DEFAULT_PIECE_VALUE = {
    "King": 100,
    "Queen": 10,
    "Rook": 6,
    "Knight": 4,
    "Bishop":3,
    "Pawn":1
}

_JUSTINIANUS_CHECKMATE_VALUE = 1000
_JUSTINIANUS_SEARCH_DEPTH = 2
_JUSTINIANUS_SEARCH_REPETITIONS = 3
_JUSTINIANUS_STALEMATE_VALUE = 0.523
_JUSITNIANUS_STOHASTIC_LIMIT = 10
_JUSTINIANUS_STOHASTIC_COEFFICIENT = 1 # DISABLED!
_JUSTINIANUS_PRUNE_LIMIT = 7
_JUSTINIANUS_PRUNE_COEFFICIENT = 0.523

