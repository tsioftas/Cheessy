from constants import BOARD_Y_DIM, BOARD_X_DIM

class Board:

    def __init__(self):
        self.x_dim = BOARD_X_DIM
        self.y_dim = BOARD_Y_DIM
        self.squares = [[None for i in range(self.x_dim)] for j in range(self.y_dim)]
