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
        assert self.is_valid_coord(), f"Cannot create invalid position [{x}, {y}] in P0."



    def is_valid_coord(self):
        return 0 <= self.x and self.x <= 7 and 0 <= self.y and self.y <= 7