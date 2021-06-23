# Battleships in a Board

# Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
# return the number of the battleships on board.

# Battleships can only be placed horizontally or vertically on board. In other
# words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1
# (k rows, 1 column), where k can be of any size. At least one horizontal or
# vertical cell separates between two battleships (i.e., there are no adjacent
# battleships).

# Example 1:

# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2

class Solution:
  def countBattleships(self, board: List[List[str]]) -> int:
    result = 0
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == 'X':
          result += 1
          self.get_battleship(board, i, j)
    return result
          
  def get_battleship(self, board: List[List[str]], i: int, j: int):
    top = i - 1
    bottom = i + 1
    left = j - 1
    right = j + 1
    while top >= 0 and board[top][j] == 'X':
      board[top][j] = None
      top -= 1
    while bottom < len(board) and board[bottom][j] == 'X':
      board[bottom][j] = None
      bottom += 1
    while left >= 0 and board[i][left] == 'X':
      board[i][left] = None
      left -= 1
    while right < len(board[0]) and board[i][right] == 'X':
      board[i][right] = None
      right += 1

# Simplified solution without modifying the board

class Solution:
  def countBattleships(self, board: List[List[str]]) -> int:
    result = 0
    for i in range(len(board)):
      for j in range(len(board[0])):
        is_x = board[i][j] == 'X'
        is_topmost = i == 0 or board[i - 1][j] == '.'
        is_leftmost = j == 0 or board[i][j - 1] == '.'
        if is_x and is_topmost and is_leftmost:
          result += 1
    return result
