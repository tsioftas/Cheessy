from algorithm import RandomAlgorithm
from chess_board import Chessboard
from chess_board_controller import ChessboardController
from chess_pieces import PieceInterface
from common_imports import List, TODO_Type
from constants import Colour
from player import Player
from graphics import GraphicsControllerHub

if __name__ == "__main__":
    graphicsControllerHub = GraphicsControllerHub()
    initialPieces: List[PieceInterface] = ChessboardController.INITIAL_PIECES
    chessboard = Chessboard(initialPieces)
    chessboardController = ChessboardController()
    player1 = Player(Colour.White, algorithm=RandomAlgorithm, seed=1)
    player2 = Player(Colour.Black, algorithm=RandomAlgorithm, seed=2)
    move_count = 0
    while True:
        # get moves and update board
        move = player1.get_next_move(chessboard)
        if move is None:
            print("Player 2 wins!")
            break
        move_count += 1
        print(f"{move_count}. Moving the {move.piece.colour} {move.piece.name} from [{move.piece.pos.x}, {move.piece.pos.y}] to [{move.destination.x}, {move.destination.y}]")
        chessboardController.applyMove(chessboard, move)
        # draw graphics
        graphicsControllerHub.display_image(chessboard)
        input()
        move = player2.get_next_move(chessboard)
        if move is None:
            print("Player 1 wins!")
            break
        move_count += 1
        print(f"{move_count}. Moving the {move.piece.colour} {move.piece.name} from [{move.piece.pos.x}, {move.piece.pos.y}] to [{move.destination.x}, {move.destination.y}]")
        chessboardController.applyMove(chessboard, move)
        # draw graphics
        graphicsControllerHub.display_image(chessboard)
        input()
        # TODO: add win check