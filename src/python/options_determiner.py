from ast import Pass
from msvcrt import getche
from turtle import undo
from bishop import Bishop
from chess_board_controller import ChessboardController
from common_imports import TODO_Type
from chess_pieces import PieceInterface
from constants import _BOARD_X_DIM, _COLOUR
import constants
from common_imports import List
from chess_board import Chessboard, Move, getChessboardCopy
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from utils import Coord
from rook import Rook

class OptionsDeterminerInterface:

    PIECE_TYPES = [King, Queen, Knight, Bishop, Rook, Pawn]

    class RookOptionsDeterminer:

        def determine_options(piece: PieceInterface, chessboard: Chessboard) -> List[Move]:
            assert type(piece) == Rook, f"Invalid type \"{type(piece)}\" given to options determiner. Expected \"Rook\""
            # Select the valid destinations given the chessboard
            valid_destinations: List[Coord] = []
            # First vertically
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_vertical_destinations(piece,
                chessboard))
            # Then horizontally
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_horizontal_destinations(piece,
                chessboard))
            return [Move(piece, new_pos) for new_pos in valid_destinations]
    
    class KnightOptionsDeterminer:

        def determine_options(piece: PieceInterface, chessboard: Chessboard) -> List[Move]:
            assert type(piece) == Knight, f"Invalid type \"{type(piece)}\" given to options determiner. Expected \"Knight\""
            # These are the possible moves for a knight
            deltas = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
            # Select the valid destinations given the chessboard
            valid_destinations: List[Coord] = []
            pos = piece.pos
            for delta_x, delta_y in deltas:
                destination_is_valid = True
                try:
                    newpos = Coord(pos.x + delta_x, pos.y + delta_y)
                except AssertionError:
                    destination_is_valid = False
                if destination_is_valid:
                    dest_piece = chessboard.squares[newpos.x][newpos.y]
                    if dest_piece is not None and dest_piece.colour == piece.colour:
                        destination_is_valid = False
                if destination_is_valid:
                    valid_destinations.append(newpos)
            return [Move(piece, new_pos) for new_pos in valid_destinations]
    
    class BishopOptionsDeterminer:

        def determine_options(piece: PieceInterface, chessboard: Chessboard) -> List[Move]:
            assert type(piece) == Bishop, f"Invalid type \"{type(piece)}\" given to options determiner. Expected \"Bishop\""
            # Select the valid destinations given the chessboard
            valid_destinations: List[Coord] = []
            # First top-left to bottom-right
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_tlbr_diagonal_destinations(piece,
                chessboard))
            # Then bottom-left to top-right
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_bltr_diagonal_destinations(piece,
                chessboard))
            return [Move(piece, new_pos) for new_pos in valid_destinations]
    
    class QueenOptionsDeterminer:

        def determine_options(piece: PieceInterface, chessboard: Chessboard) -> List[Move]:
            assert type(piece) == Queen, f"Invalid type \"{type(piece)}\" given to options determiner. Expected \"Queen\""
            # Select the valid destinations given the chessboard
            valid_destinations: List[Coord] = []
            # First top-left to bottom-right
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_tlbr_diagonal_destinations(piece,
                chessboard))
            # Then bottom-left to top-right
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_bltr_diagonal_destinations(piece,
                chessboard))
            # Also vertically
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_vertical_destinations(piece,
                chessboard))
            # And horizontally
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_horizontal_destinations(piece,
                chessboard))
            return [Move(piece, new_pos) for new_pos in valid_destinations]
    
    class PawnOptionsDeterminer:

        def determine_options(piece: PieceInterface, chessboard: Chessboard) -> List[Move]:
            assert type(piece) == Pawn, f"Invalid type \"{type(piece)}\" given to options determiner. Expected \"Pawn\""
            # Select the valid destinations given the chessboard
            valid_destinations: List[Coord] = []
            # Determine forward direction based on colour
            forward = -1 if piece.colour == _COLOUR.White else 1
            # One forward
            one_f = Coord(piece.pos.x+forward, piece.pos.y)
            if chessboard.squares[one_f.x][one_f.y] is None:
                # square is empty, move can be made
                valid_destinations.append(one_f)
                if not piece.first_move_done:
                    # could move two squares
                    two_f = Coord(piece.pos.x+2*forward, piece.pos.y)
                    if chessboard.squares[two_f.x][two_f.y] is None:
                        valid_destinations.append(two_f)
                if piece.pos.y > 0:
                    one_f_l = Coord(piece.pos.x + forward, piece.pos.y-1)
                    target = chessboard.squares[one_f_l.x][one_f_l.y] 
                    if target is not None and target.colour != piece.colour:
                        valid_destinations.append(one_f_l)
                if piece.pos.y < constants._BOARD_Y_DIM-1:
                    one_f_r = Coord(piece.pos.x + forward, piece.pos.y+1)
                    target = chessboard.squares[one_f_r.x][one_f_r.y] 
                    if target is not None and target.colour != piece.colour:
                        valid_destinations.append(one_f_r)
            ret = []
            for new_pos in valid_destinations:
                promotions = [Bishop, Rook, Knight, Queen]
                if new_pos.x == 0 or new_pos.x == constants._BOARD_X_DIM-1:
                    # Pawn is promoted
                    for replacement_piece in promotions:
                        ret.append(Move(piece, new_pos, replacement_piece))
                else:
                    ret.append(Move(piece, new_pos))
            return ret

    class KingOptionsDeterminer:

        def determine_options(piece: PieceInterface, chessboard: Chessboard) -> List[Move]:
            assert type(piece) == King, f"Invalid type \"{type(piece)}\" given to options determiner. Expected \"King\""
            # Select the valid destinations given the chessboard
            valid_destinations: List[Coord] = []
            adds = [-1, 0, 1]
            candidates = []
            for i in adds:
                for j in adds:
                    if i == 0 and j == 0:
                        continue
                    cand_x = piece.pos.x + i
                    cand_y = piece.pos.y + j
                    if 0 <= cand_x and cand_x <= constants._BOARD_X_DIM-1 and \
                       0 <= cand_y and cand_y <= constants._BOARD_Y_DIM-1:
                       candidates.append(Coord(cand_x, cand_y))
            for candidate in candidates:
                target = chessboard.squares[candidate.x][candidate.y]
                if target is None or target.colour != piece.colour:
                    # TODO: check for check
                    # if destination not in check 
                    valid_destinations.append(Move(piece, candidate))
            return valid_destinations 

    def __get_sequential_movement_destinations(destinations: List[Coord], piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        x = piece.pos.x
        y = piece.pos.y
        buffer: List[Coord] = []
        valid_destinations: List[Coord] = []
        # Move from 0 to pos-1
        i = 0
        while True:
            current_pos = destinations[i]
            if current_pos is None:
                i += 1
                continue
            elif destinations[i].x == x and destinations[i].y == y:
                break
            if chessboard.squares[current_pos.x][current_pos.y] is not None:
                buffer = [current_pos] if chessboard.squares[current_pos.x][current_pos.y].colour != piece.colour else []
            else:
                buffer.append(current_pos)
            i += 1
        valid_destinations.extend(buffer)
        buffer = []
        # Move from pos+1 to BOARD_X_DIM-1
        i += 1
        while i < len(destinations):
            current_pos = destinations[i]
            if current_pos is None:
                i += 1
                continue
            if chessboard.squares[current_pos.x][current_pos.y] is not None:
                if chessboard.squares[current_pos.x][current_pos.y].colour != piece.colour:
                    buffer.append(current_pos)
                break
            else:
                buffer.append(current_pos)
            i += 1
        valid_destinations.extend(buffer)
        return valid_destinations

    def __get_tlbr_diagonal_destinations(piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        x = piece.pos.x
        y = piece.pos.y
        k = x-y # this is constant along the main diagonal
        tlbr_diagonal_destinations = [Coord.create_valid_coord(i,i-k) for i in range(constants._BOARD_X_DIM)]
        return OptionsDeterminerInterface.__get_sequential_movement_destinations(tlbr_diagonal_destinations, piece, chessboard)
    
    def __get_bltr_diagonal_destinations(piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        x = piece.pos.x
        y = piece.pos.y
        k = x+y # this is constant along the main diagonal
        bltr_diagonal_destinations = [Coord.create_valid_coord(i,k-i) for i in range(constants._BOARD_X_DIM)]
        return OptionsDeterminerInterface.__get_sequential_movement_destinations(bltr_diagonal_destinations, piece, chessboard)
        
    
    def __get_vertical_destinations(piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        y = piece.pos.y
        vertical_destinations = [Coord(i,y) for i in range(constants._BOARD_X_DIM)]
        return OptionsDeterminerInterface.__get_sequential_movement_destinations(vertical_destinations, piece, chessboard)
        

    def __get_horizontal_destinations(piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        x = piece.pos.x
        horizontal_destinations = [Coord(x,i) for i in range(constants._BOARD_Y_DIM)]
        return OptionsDeterminerInterface.__get_sequential_movement_destinations(horizontal_destinations, piece, chessboard)


    determiner_map = {
        Rook: RookOptionsDeterminer,
        Knight: KnightOptionsDeterminer,
        Bishop: BishopOptionsDeterminer,
        Pawn: PawnOptionsDeterminer,
        Queen: QueenOptionsDeterminer,
        King: KingOptionsDeterminer
    }

    def gives_up_king(move: Move, chessboard: Chessboard):
        import copy
        chessboard_copy = getChessboardCopy(chessboard)
        moving_player = move.piece.colour
        other_player = {
            _COLOUR.White: _COLOUR.Black,
            _COLOUR.Black: _COLOUR.White
        }[moving_player]
        cc = ChessboardController()
        piece_copy = chessboard_copy.squares[move.piece.pos.x][move.piece.pos.y]
        move_copy = Move(piece_copy, move.destination)
        cc.applyMove(chessboard_copy, move_copy)
        own_king = chessboard_copy.getPieces(moving_player, King)
        ret = False
        if own_king != []:
            # TODO: arbitrary, might cause issues if game rules are modified (e.g. 2 kings)
            own_king = own_king[0]
            enemy_moves = OptionsDeterminerInterface.determine_options(other_player, chessboard_copy, check_for_check=False)
            for enemy_move in enemy_moves:
                destination = enemy_move.destination
                if destination.x == own_king.pos.x and destination.y == own_king.pos.y:
                    # own_king is threatened by enemy_move
                    ret = True
        return ret
    
    def remove_options_with_check(options: List[Move], chessboard: Chessboard):
        if options is None or len(options) == 0:
            return
        to_remove = []
        for move in options:
            if OptionsDeterminerInterface.gives_up_king(move, chessboard):
                to_remove.append(move)
        for to_re_move in to_remove:
            options.remove(to_re_move)          

    def determine_options(turnColour: _COLOUR, chessboard: Chessboard, check_for_check = True) -> List[Move]:
        player_options = []
        pieces = chessboard.pieces
        for piece in pieces:
            if piece.colour == turnColour:
                t = type(piece)
                piece_options = OptionsDeterminerInterface.determiner_map[t].determine_options(piece, chessboard)
                if check_for_check:
                    debug_piece_x = None
                    debug_piece_y = None
                    debug_piece = piece.pos.x == debug_piece_x and piece.pos.y == debug_piece_y
                    if debug_piece:
                        print(f"[DEBUG] Debug piece options before remove_options_with_check: {piece_options}")
                        num_options = len(piece_options)
                    OptionsDeterminerInterface.remove_options_with_check(piece_options, chessboard)
                    if debug_piece:
                        print(f"[DEBUG] ...and after: {piece_options}")
                        removed_options = num_options - len(piece_options)
                        if removed_options != 0:
                            print(f"[DEBUG] {removed_options} options were removed!")
                player_options.extend(piece_options)
        # if check_for_check:
        #     print(f"{turnColour} Player Options: {player_options}s")
        return player_options

    
