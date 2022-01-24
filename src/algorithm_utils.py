
from shutil import move
from chess_board import Chessboard

from chess_board_controller import ChessboardController, Move
from chess_board import Chessboard, Move, getChessboardCopy
from king import King
from options_determiner import OptionsDeterminerInterface
from constants import _COLOUR, _OTHER_TURN_COLOUR, _CHESS_TERMS

__cc = ChessboardController()

def applyMoveToCopy(chessboard: Chessboard, move: Move) -> Chessboard:
    chessboard_copy = getChessboardCopy(chessboard)
    piece_copy = chessboard_copy.squares[move.piece.pos.x][move.piece.pos.y]
    move_copy = Move(piece_copy, move.destination)
    __cc.applyMove(chessboard_copy, move_copy)
    return chessboard_copy

def getMoveType(move: Move, chessboard: Chessboard) -> _CHESS_TERMS:
    chessboard_copy = applyMoveToCopy(chessboard, move)
    current_player: _COLOUR = move.piece.colour
    other_player: _COLOUR = _OTHER_TURN_COLOUR[current_player]
    # 1. Does the other player have an available move?
    other_player_options = OptionsDeterminerInterface.determine_options(other_player, chessboard_copy)
    if other_player_options != []:
        return False
    # 2. The other player has no available move. Is this a stalemate or a checkmate?
    # TODO: assumption for one king
    other_king_pos = chessboard_copy.getPieces(other_player, King)[0].pos
    potential_moves = OptionsDeterminerInterface.determine_options(current_player, chessboard_copy, check_for_check=False)
    potential_moves_destinations = [m.destination for m in potential_moves]
    threatens_king = other_king_pos in potential_moves_destinations
    print(f"Threatened squares by {current_player}: {potential_moves_destinations}")
    print(f"{other_player} King is at {other_king_pos}")
    if threatens_king:
        return _CHESS_TERMS.CHECKMATE
    else:
        return _CHESS_TERMS.STALEMATE
    