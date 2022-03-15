from msvcrt import getche
from random import Random
import numpy as np

from stockfish import Stockfish

from algorithm import Justinianus, RandomAlgorithm, SharedResources, Pletho, Socrates
from chess_board import Chessboard, getChessboardCopy
from chess_board_controller import ChessboardController
from chess_pieces import PieceInterface
from common_imports import List, TODO_Type
from constants import _COLOUR, _BOARD_X_DIM, _BOARD_Y_DIM
from player import Player
from graphics import GraphicsControllerHub
from chessboard_data_manipulator import ChessboardDataManinpulator
import algorithm_utils as au
from algorithm import Ichtys
from randomwisdom import WiseOne

def run_game():
    # Greetings
    oracle = WiseOne()
    print(f"The wise one says: {oracle.getSaying()}")

    graphicsControllerHub = GraphicsControllerHub(300)
    initialPieces: List[PieceInterface] = ChessboardController.INITIAL_PIECES
    chessboard = Chessboard(initialPieces)
    chessboardController = ChessboardController()
    shared_resources = SharedResources()

    # load data
    filename = "data/data_smart.npy"
    justinianus_for_labelling = Justinianus(_COLOUR.White, np.random.randint(0, 9999999), shared_resources=SharedResources())
    chessboard_data_manipulator = ChessboardDataManinpulator(filename, _BOARD_X_DIM, _BOARD_Y_DIM, justinianus_for_labelling)
    # select and initialize algorithms for each player
    colours = [_COLOUR.White, _COLOUR.Black]
    # c1 = np.random.randint(0,2)
    init_state_str = chessboard_data_manipulator.datum_to_string(chessboard_data_manipulator.chessboard_to_datum(chessboard))
    data_dict = chessboard_data_manipulator.np_to_dict(chessboard_data_manipulator.data)
    init_state_data = data_dict.get(init_state_str, 0)
    more_white_wins = init_state_data[1] > init_state_data[2]
    c1 = 1 if more_white_wins else 0
    players = [# Player(colours[c1], algorithm=Pletho, seed=1, data_manipulator=chessboard_data_manipulator),
               Player(colours[c1], algorithm=Ichtys, path='stockfish/stockfish_14.1_win_x64_avx2.exe'),
               # Player(colours[1-c1], algorithm=Socrates)]
               # Player(colours[1-c1], algorithm=Justinianus, seed=2, shared_resources=shared_resources)]
               Player(colours[1-c1], algorithm=Pletho, seed=2, data_manipulator=chessboard_data_manipulator)]
    p1 = 0 if players[0].colour == _COLOUR.White else 1
    if p1 == 0:
        print("Pletho is player 2")
    else:
        print("Pletho is player 1")
    player1 = players[p1]
    player2 = players[1-p1]
    print(f"Player1: {player1.colour}")
    print(f"Player2: {player2.colour}")
    #player2 = Player(_COLOUR.Black, algorithm=RandomAlgorithm, seed=np.random.randint(0, 1000000))
    # initialize game statistic and other variables
    move_count = 0
    game_history = [getChessboardCopy(chessboard)]
    winner = None
    while True:
        # draw graphics
        graphicsControllerHub.display_image(chessboard)
        # get moves and update board
        move = player1.get_next_move(chessboard)
        if move is None:
            print("Player 2 wins!")
            winner = player2.colour
            break
        move_count += 1
        print(f"{move_count}. Moving the {move.piece.colour} {move.piece.name} from [{move.piece.pos.x}, {move.piece.pos.y}] to [{move.destination.x}, {move.destination.y}]")
        if not player1.algorithm.shared_resources is None:
            chessboard = shared_resources.current_state.chessboard
        else:
            chessboard = au.applyMoveToCopy(chessboard, move)
            if not player2.algorithm.shared_resources is None:
                if shared_resources.current_state is None:
                    shared_resources.recursion_tree = au.RecursionTree()
                    shared_resources.recursion_tree.initialize_tree(chessboard, player1.colour, player2.algorithm.valfunction)
                    shared_resources.current_state = shared_resources.recursion_tree.root
                else:
                    shared_resources.current_state = shared_resources.current_state.expand(chosen_move=move)
        game_history.append(getChessboardCopy(chessboard))
        player1.algorithm.update(move)
        player2.algorithm.update(move)
        # draw graphics
        graphicsControllerHub.display_image(chessboard)
        move = player2.get_next_move(chessboard)
        if move is None:
            print("Player 1 wins!")
            winner = player1.colour
            break
        move_count += 1
        print(f"{move_count}. Moving the {move.piece.colour} {move.piece.name} from [{move.piece.pos.x}, {move.piece.pos.y}] to [{move.destination.x}, {move.destination.y}]")
        if not player2.algorithm.shared_resources is None:
            chessboard = shared_resources.current_state.chessboard
        else:
            chessboard = au.applyMoveToCopy(chessboard, move)
            if not player1.algorithm.shared_resources is None:
                if shared_resources.current_state is None:
                    # chessboardController.applyMove(chessboard, move)
                    shared_resources.recursion_tree = au.RecursionTree()
                    shared_resources.recursion_tree.initialize_tree(chessboard, player1.colour, player1.algorithm.valfunction)
                    shared_resources.current_state = shared_resources.recursion_tree.root
                else:
                    shared_resources.current_state = shared_resources.current_state.expand(chosen_move=move)
        game_history.append(getChessboardCopy(chessboard))
        player1.algorithm.update(move)
        player2.algorithm.update(move)
        # draw graphics
        graphicsControllerHub.display_image(chessboard)
        # TODO: add win check
    print("Do you wish to save this game's data to the dataset? (default yes, n for no): ", end="")
    print("FORCE-SAVE-ON!")
    x = 'y'# input()
    if x != 'n':
        print("Saving game data...")
        chessboard_data_manipulator.update_and_save_data(filename, game_history, winner)
    print("Goodbye.")

if __name__ == "__main__":
    counter = 0
    try:
        while True:
            run_game()
            counter += 1
    except KeyboardInterrupt:
        print(f"\nInterrupted after {counter} games.")