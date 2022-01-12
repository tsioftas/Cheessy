import cv2 as cv
import numpy as np
import os

from chess_board import Chessboard
from chess_pieces import PieceInterface
from constants import ASSETS_PATH, Colour,\
    WHITE_SQUARE_ASSET, BLACK_SQUARE_ASSET, \
    WHITE_ROOK_ASSET, BLACK_ROOK_ASSET, \
    WHITE_KNIGHT_ASSET, BLACK_KNIGHT_ASSET, \
    WHITE_BISHOP_ASSET, BLACK_BISHOP_ASSET, \
    WHITE_PAWN_ASSET, BLACK_PAWN_ASSET
from common_imports import Rook
from knight import Knight
from bishop import Bishop
from pawn import Pawn

"""
To be used to bring together and coordinate all graphics items.
"""
class GraphicsControllerHub:
    
    def __init__(self):
        self.chessboardGC = ChessboardGraphicsController(ASSETS_PATH)
    
    def display_image(self, chessboard: Chessboard):
        image = self.chessboardGC.chessboardToImage(chessboard)
        cv.imshow('board', image)
        cv.waitKey(1)

"""
To be used as the parent class of graphics controllers. Not to be instantiated!
"""
class GraphicsControllerInterface:
    
    def __init__(self, assets_path: str):
        self.assets_path = assets_path
    
    def get_asset(self, asset: str):
        return cv.imread(os.path.join(self.assets_path, asset), cv.IMREAD_UNCHANGED)


"""
To manage all rook-related graphics tasks.
"""
class RookGraphicsController(GraphicsControllerInterface):

    def __init__(self, assets_path: str):
        super().__init__(assets_path)
        self.white_rook_img = self.get_asset(WHITE_ROOK_ASSET)
        self.black_rook_img = self.get_asset(BLACK_ROOK_ASSET)

    def get_image(self, rook):
        if rook.colour == Colour.White:
            return self.white_rook_img
        else:
            return self.black_rook_img

"""
To manage all knight-related graphics tasks.
"""
class KnightGraphicsController(GraphicsControllerInterface):

    def __init__(self, assets_path: str):
        super().__init__(assets_path)
        self.white_knight_img = self.get_asset(WHITE_KNIGHT_ASSET)
        self.black_knight_img = self.get_asset(BLACK_KNIGHT_ASSET)

    def get_image(self, knight):
        if knight.colour == Colour.White:
            return self.white_knight_img
        else:
            return self.black_knight_img

"""
To manage all bishop-related graphics tasks.
"""
class BishopGraphicsController(GraphicsControllerInterface):

    def __init__(self, assets_path: str):
        super().__init__(assets_path)
        self.white_bishop_img = self.get_asset(WHITE_BISHOP_ASSET)
        self.black_bishop_img = self.get_asset(BLACK_BISHOP_ASSET)

    def get_image(self, bishop):
        if bishop.colour == Colour.White:
            return self.white_bishop_img
        else:
            return self.black_bishop_img

"""
To manage all pawn-related graphics tasks.
"""
class PawnGraphicsController(GraphicsControllerInterface):

    def __init__(self, assets_path: str):
        super().__init__(assets_path)
        self.white_pawn_img = self.get_asset(WHITE_PAWN_ASSET)
        self.black_pawn_img = self.get_asset(BLACK_PAWN_ASSET)

    def get_image(self, pawn):
        if pawn.colour == Colour.White:
            return self.white_pawn_img
        else:
            return self.black_pawn_img


"""
To manage all chessboard-related graphics tasks.
"""
class ChessboardGraphicsController(GraphicsControllerInterface):

    def __init__(self, assets_path: str):
        super().__init__(assets_path)
        self.white_square_img = self.get_asset(WHITE_SQUARE_ASSET)
        self.black_square_img = self.get_asset(BLACK_SQUARE_ASSET)
        self.square_x_dim, self.square_y_dim, _ = self.white_square_img.shape

    def chessboardToImage(self, chessboard: Chessboard):
        chessboard_img_x_dim = self.square_x_dim * chessboard.x_dim
        chessboard_img_y_dim = self.square_y_dim * chessboard.y_dim
        chessboard_img = np.zeros((chessboard_img_x_dim, chessboard_img_y_dim, 4))
        squares = [self.white_square_img, self.black_square_img]
        p = 0 # start with white on top-left
        for row in range(chessboard.x_dim):
            for column in range(chessboard.y_dim):
                top_left = (row*self.square_x_dim, column*self.square_y_dim)
                bottom_right_outer = (top_left[0] + self.square_x_dim, top_left[1] + self.square_y_dim)
                chessboard_img[top_left[0]:bottom_right_outer[0], top_left[1]:bottom_right_outer[1], :] = squares[p]
                p = 1-p
            p = 1-p
        for piece in chessboard.pieces:
            chessboard_img = self.paint_piece(piece, chessboard_img)
        return chessboard_img
    
    def image_from_piece(self, piece: PieceInterface):
        t = type(piece)
        graphics_controller_dict = {
            Rook: RookGraphicsController(self.assets_path),
            Knight: KnightGraphicsController(self.assets_path),
            Bishop: BishopGraphicsController(self.assets_path),
            Pawn: PawnGraphicsController(self.assets_path)
        }
        gc = graphics_controller_dict[t]
        assert gc, f"No graphics found for piece of type \"{t}\""
        return gc.get_image(piece)

    def paint_piece(self, piece: PieceInterface, chessboard_img):
        img = self.image_from_piece(piece)
        x = piece.pos.x
        y = piece.pos.y
        top_left = (x*self.square_x_dim, y*self.square_y_dim)
        bottom_right_outer = (top_left[0] + self.square_x_dim, top_left[1] + self.square_y_dim)
        sq = chessboard_img[top_left[0]:bottom_right_outer[0], top_left[1]:bottom_right_outer[1], :]
        alpha = img[:, :, 3]
        for i in range(4):
            sq[:, :, i] = (255-alpha)*sq[:, :, i] + alpha*img[:, :, i]
        return chessboard_img