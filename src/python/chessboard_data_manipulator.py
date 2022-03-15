import os
from re import A
from typing import Dict, List, Tuple
import numpy as np

from constants import _COLOUR, _BOARD_X_DIM, _BOARD_Y_DIM
from chess_board import Chessboard

class ChessboardDataManinpulator:

    def __init__(self, filename: str, board_x_dim: int, board_y_dim: int, justinianus):
        self.justinianus = justinianus
        self.filename = filename
        self.board_x_dim = board_x_dim
        self.board_y_dim = board_y_dim
        w = _COLOUR.White
        b = _COLOUR.Black
        pieces = ["King", "Queen", "Rook", "Knight", "Bishop", "Pawn"]
        colours = [w, b]
        self.piece_to_label = {}
        self.label_to_char = {
            0: '.' # empty square
        }
        self.char_to_label = {
            '.': 0
        }
        self.piece_to_char = {
            "King": 'K',
            "Queen": 'Q',
            "Rook": 'R',
            "Knight": 'N',
            "Bishop": 'B',
            "Pawn": 'P'
        }
        label = 1
        for colour in colours:
            for piece in pieces:
                self.piece_to_label[(colour, piece)] = label
                pchar = self.piece_to_char[piece]
                if colour == _COLOUR.White:
                    pchar = pchar.upper()
                elif colour == _COLOUR.Black:
                    pchar = pchar.lower()
                else:
                    raise Exception(f"Unknown colour: {colour}")
                self.label_to_char[label] = pchar
                self.char_to_label[pchar] = label
                label += 1
        self.n_metadata = 5
        self.data = self.load_data()
    
    def chessboard_to_datum(self, chessboard) -> np.ndarray:
        datum = np.zeros((chessboard.x_dim, chessboard.y_dim))
        for piece in chessboard.pieces:
            pos = piece.pos
            datum[pos.x, pos.y] = self.piece_to_label[(piece.colour, piece.name)]
        return datum

    def datum_to_string(self, datum: np.ndarray):
        ret = ""
        for label in datum.flatten():
            ret += self.label_to_char[label]
        return ret
    
    def datum_from_string(self, datum_str: str) -> List[int]:
        ret = []
        for ch in datum_str:
            ret.append(self.char_to_label[ch])
        return ret

    def  np_to_dict(self, data: Tuple[np.ndarray, np.ndarray]) -> Dict[str, int]:
        data_x, data_y = data
        dictionary = {}
        for i in range(data_x.shape[0]):
            datum = data_x[i,:]
            datum_y = data_y[i]
            datum_str = self.datum_to_string(datum)
            dictionary[datum_str] = datum_y
        return dictionary
    
    def dict_to_np(self, dictionary: Dict[str, List[int]]) -> np.ndarray:
        ret_x = []
        ret_y = []
        for datum_str, metadata in dictionary.items():
            datum = self.datum_from_string(datum_str)
            ret_x.append(datum)
            ret_y.append(metadata)
        return np.array(ret_x), np.array(ret_y)
            
    def load_data(self) -> Tuple[np.ndarray, np.ndarray]:
        filename = self.filename
        board_x_dim = self.board_x_dim
        board_y_dim = self.board_y_dim
        try:
            with open(filename, "rb") as f:
                data: np.ndarray = np.load(f, allow_pickle=True)
        except:
            return np.zeros((1, _BOARD_X_DIM*_BOARD_Y_DIM)), np.zeros((1, self.n_metadata))
        N, D = data.shape
        assert D == board_x_dim*board_y_dim+self.n_metadata
        data_x = data[:, :-self.n_metadata].reshape((N, board_x_dim, board_y_dim))
        data_y = data[:,-self.n_metadata:]
        print(f"Loaded {N} datapoints")
        return data_x, data_y

    def update_and_save_data(self,
                             filename: str, 
                             game_history: List[Chessboard],
                             winner: _COLOUR):
        data_dict = self.np_to_dict(self.data)
        white_win = 1 if winner == _COLOUR.White else 0 if winner == _COLOUR.Black else 0
        black_win = 1-white_win
        player, opponent = _COLOUR.White, _COLOUR.Black
        for i, chessboard in enumerate(game_history):
            datum = self.chessboard_to_datum(chessboard)
            datum_str = self.datum_to_string(datum)
            if not datum_str in data_dict:
                rt = self.justinianus.create_recursion_tree(chessboard, opponent)
                justinianus_simple_valfunction = self.justinianus.get_simple_valfunction()
                justinianus_evaluation = justinianus_simple_valfunction(rt.root)
                white_wins_count = white_win
                black_wins_count = black_win
                avg_percent_i_white = white_win * i
                avg_percent_i_black = black_win * i
                data_dict[datum_str] = [justinianus_evaluation, white_wins_count, black_wins_count, avg_percent_i_white, avg_percent_i_black]
            else:
                d = data_dict[datum_str]
                justinianus_evaluation, white_wins_count, black_wins_count, avg_percent_i_white, avg_percent_i_black = (0,1,2,3,4)
                d[white_wins_count] += white_win
                d[black_wins_count] += black_win
                if white_win == 1:
                    d[avg_percent_i_white] = (d[avg_percent_i_white] * (d[white_wins_count] -1) + i) / d[white_wins_count]
                else:
                    d[avg_percent_i_black] = (d[avg_percent_i_black] * (d[black_wins_count] -1) + i) / d[black_wins_count]
            opponent, player = player, opponent
        self.data = self.dict_to_np(data_dict)
        to_save = np.zeros((self.data[0].shape[0], self.data[0].shape[1]+self.n_metadata))
        to_save[:,:-self.n_metadata] = self.data[0]
        to_save[:,-self.n_metadata:] = self.data[1]
        print(f"Saving data with shape: {to_save.shape}")
        with open(filename, "wb") as f:
            np.save(f, to_save)
        return



