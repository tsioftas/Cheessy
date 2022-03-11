# ifndef UTILS_H
# define UTILS_H

# include "constants.h"

/**
 * Stores coordinates in a chessboard.
 */
class Coord
{
    private:
    int x;
    int y;

    public:
    //**
     * @brief Construct a new Coord object
     * 
     * @param x, y the coordinates that the new object represents
     */
    Coord(int x, int y);

    //**
     * @brief Creates a Coord object only if the provided coordinates are valid.
     *
     * The coordinates are valid if they are both within the bounds as defined in
     * "constants.h"
     * 
     * @param x, y the coordinates that the new object represents
     * @returns Coord the new object
     * @returns nullptr if the given coordinates were invalid
     */
    static Coord create_valid_coord(int x, int y);

    //**
     * @brief Returns a string representation of the caller's coordinates in the form "(x,y)"
     * 
     * @return string representation of the caller
     */
    string to_string();

    private:
    //**
     * @brief Returns true if the caller is a valid coordinate.
     *
     * A coordinate is valid if both its x and y components are within
     * the range specified in "constants.h".
     * 
     * @returns true If the caller is a Coordinate object representing a
     * valid chessboard coordinate
     * @returns false Otherwise.
     */
    bool is_valid_coord();

};

# endif