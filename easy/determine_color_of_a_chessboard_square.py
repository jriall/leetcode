# Determine Color of a Chessboard Square

# You are given coordinates, a string that represents the coordinates of a
# square of the chessboard. Below is a chessboard for your reference.

# Return true if the square is white, and false if the square is black.

# The coordinate will always represent a valid chessboard square. The coordinate
# will always have the letter first, and the number second.

# Example 1:

# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is
# black, so return false.

class Solution:
  def squareIsWhite(self, coordinates: str) -> bool:
    cols = ['a', 'b', 'c', 'd', 'e',  'f', 'g', 'h']
    return (cols.index(coordinates[0]) + int(coordinates[1])) % 2 == 0