import enum

Colour = enum.Enum("Colours", "Black White")

# Chessboard layout constants
BOARD_Y_DIM = 8
BOARD_X_DIM = 8

# Graphics-related constants
DISPLAY_HEIGHT = 800
DISPLAY_WIDTH = 600
ASSETS_PATH = "assets"
BLACK_SQUARE_ASSET = "black_square.png"
WHITE_SQUARE_ASSET = "white_square.png"
BLACK_ROOK_ASSET = "black_rook.png"
WHITE_ROOK_ASSET = "white_rook.png"