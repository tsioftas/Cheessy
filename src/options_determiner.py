from bishop import Bishop
from common_imports import TODO_Type
from chess_pieces import PieceInterface
from constants import Colour
import constants
from common_imports import List
from chess_board import Chessboard, Move
from knight import Knight
from pawn import Pawn
from utils import Coord
from rook import Rook

class OptionsDeterminerInterface:

    class RookOptionsDeterminer:

        def determine_options(piece: PieceInterface, pieces: List[PieceInterface], chessboard: Chessboard) -> List[Coord]:
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

        def determine_options(piece: PieceInterface, pieces: List[PieceInterface], chessboard: Chessboard) -> List[Coord]:
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

        def determine_options(piece: PieceInterface, pieces: List[PieceInterface], chessboard: Chessboard) -> List[Coord]:
            assert type(piece) == Bishop, f"Invalid type \"{type(piece)}\" given to options determiner. Expected \"Bishop\""
            # Select the valid destinations given the chessboard
            valid_destinations: List[Coord] = []
            # First vertically
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_tlbr_diagonal_destinations(piece,
                chessboard))
            # Then horizontally
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_bltr_diagonal_destinations(piece,
                chessboard))
            return [Move(piece, new_pos) for new_pos in valid_destinations]
    
    class PawnOptionsDeterminer:

        def determine_options(piece: PieceInterface, pieces: List[PieceInterface], chessboard: Chessboard) -> List[Coord]:
            assert type(piece) == Bishop, f"Invalid type \"{type(piece)}\" given to options determiner. Expected \"Bishop\""
            # Select the valid destinations given the chessboard
            valid_destinations: List[Coord] = []
            # First vertically
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_tlbr_diagonal_destinations(piece,
                chessboard))
            # Then horizontally
            valid_destinations.extend(OptionsDeterminerInterface._OptionsDeterminerInterface__get_bltr_diagonal_destinations(piece,
                chessboard))
            return [Move(piece, new_pos) for new_pos in valid_destinations]

    def __get_sequential_movement_destinations(destinations: List[Coord], piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        x = piece.pos.x
        y = piece.pos.y
        buffer: List[Coord] = []
        valid_destinations: List[Coord] = []
        # Move from 0 to x-1
        for i in range(x):
            current_pos = destinations[i]
            if current_pos is None:
                continue
            if chessboard.squares[current_pos.x][current_pos.y] is not None:
                buffer = [current_pos] if chessboard.squares[current_pos.x][current_pos.y].colour != piece.colour else []
            else:
                buffer.append(current_pos)
        valid_destinations.extend(buffer)
        buffer = []
        # Move from x+1 to BOARD_X_DIM-1
        for i in range(x+1,constants.BOARD_X_DIM):
            current_pos = destinations[i]
            if current_pos is None:
                continue
            if chessboard.squares[current_pos.x][current_pos.y] is not None:
                if chessboard.squares[current_pos.x][current_pos.y].colour != piece.colour:
                    buffer.append(current_pos)
                break
            else:
                buffer.append(current_pos)
        valid_destinations.extend(buffer)
        return valid_destinations

    def __get_tlbr_diagonal_destinations(piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        x = piece.pos.x
        y = piece.pos.y
        k = x-y # this is constant along the main diagonal
        tlbr_diagonal_destinations = [Coord.create_valid_coord(i,i-k) for i in [j for j in range(constants.BOARD_X_DIM)]]
        return OptionsDeterminerInterface.__get_sequential_movement_destinations(tlbr_diagonal_destinations, piece, chessboard)
    
    def __get_bltr_diagonal_destinations(piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        x = piece.pos.x
        y = piece.pos.y
        k = x+y # this is constant along the main diagonal
        bltr_diagonal_destinations = [Coord.create_valid_coord(i,k-i) for i in [j for j in range(constants.BOARD_X_DIM)]]
        return OptionsDeterminerInterface.__get_sequential_movement_destinations(bltr_diagonal_destinations, piece, chessboard)
        
    
    def __get_vertical_destinations(piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        y = piece.pos.y
        vertical_destinations = [Coord(i,y) for i in [j for j in range(constants.BOARD_X_DIM)]]
        return OptionsDeterminerInterface.__get_sequential_movement_destinations(vertical_destinations, piece, chessboard)
        

    def __get_horizontal_destinations(piece: PieceInterface, chessboard: Chessboard) -> List[Coord]:
        x = piece.pos.x
        horizontal_destinations = [Coord(x,i) for i in [j for j in range(constants.BOARD_Y_DIM)]]
        return OptionsDeterminerInterface.__get_sequential_movement_destinations(horizontal_destinations, piece, chessboard)


    determiner_map = {
        Rook: RookOptionsDeterminer,
        Knight: KnightOptionsDeterminer,
        Bishop: BishopOptionsDeterminer,
        Pawn: PawnOptionsDeterminer
    }
    
    def determine_options(turnColour: Colour, chessboard: Chessboard) -> List[Coord]:
        options = []
        pieces = chessboard.pieces
        for piece in pieces:
            if piece.colour == turnColour:
                t = type(piece)
                options.extend(OptionsDeterminerInterface.determiner_map[t].determine_options(piece, pieces, chessboard))
        return options

    
