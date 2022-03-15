import constants

# Call V0 the top-down view of the board where [0,0] is the top-left corner and white initial pieces
# are at the bottom. X-coordinates increase from top to bottom and y-coordinates from left to right.
"""
This class is to store coordinate variables. Coordinates are stored 
in matrix index form in V0. High-level methods
can be used to retrieve the coordinates in different systems.
"""
class Coord:

    """
    Constructor for coordinate class.

    x (int): the row number in V0. An integer in the range [0,7]
    y (int): the columnt number in V0. An integer in the range [0,7]
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        valid = self.is_valid_coord()
        assert valid, f"Cannot create invalid position [{x}, {y}] in P0."

    def is_valid_coord(self):
        return 0 <= self.x and self.x <= 7 and 0 <= self.y and self.y <= 7
    
    @staticmethod
    def create_valid_coord(x: int, y: int):
        if 0 <= x and x <= 7 and 0 <= y and y <= 7:
            return Coord(x, y)
        else:
            return None
        
    def __str__(self):
        return f"Coord({self.x}, {self.y})"
    
    def __repr__(self):
        return str(self)
    
    def to_chess_notation(self):
        col = col_to_chess_notation(self.y)
        row = row_to_chess_notation(self.x)
        return f"{col}{row}"

def col_to_chess_notation(y: int) -> str:
    return chr(ord('a')+y)

def row_to_chess_notation(x: int) -> str:
    return str(constants._BOARD_X_DIM-x)

def chess_notation_to_col(c: str) -> int:
    return ord(c) - ord('a')

def chess_notation_to_row(c: str) -> int:
    return constants._BOARD_X_DIM - int(c)