# Call V0 the top-down view of the board where [0,0] is the top-left corner and white is at the bottom
"""
This class is to store coordinate variables. Coordinates are stored 
in matrix index form in P0. High-level methods
can be used to retrieve the coordinates in different systems.
"""
class Coord:

    """
    Constructor for coordinate class.

    row (int): the row number in P0. An integer in the range [0,7]
    col (int): the columnt number in P0. An integer in the range [0,7]
    """
    def __init__(self, row: int, col: int):
        assert 0 <= row + column and row + column <= 14, f"Cannot create invalid position [{row}, {column}] in P0."
        self.row = row
        self.col = col
