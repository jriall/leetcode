# Max Increase to Keep City Skyline

# In a 2 dimensional array grid, each value grid[i][j] represents the height of
# a building located there. We are allowed to increase the height of any number
# of buildings, by any amount (the amounts can be different for different
# buildings). Height 0 is considered to be a building as well. 

# At the end, the "skyline" when viewed from all four directions of the grid,
# i.e. top, bottom, left, and right, must be the same as the skyline of the
# original grid. A city's skyline is the outer contour of the rectangles formed
# by all the buildings when viewed from a distance. See the following example.

# What is the maximum total sum that the height of the buildings can be
# increased?

# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: 
# The grid is:
# [ [3, 0, 8, 4], 
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]

# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]

# The grid after increasing the height of buildings without affecting skylines
# is:

# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

class Solution:
  def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    max_of_rows = []
    max_of_cols = [0 for num in grid[0]]#
    result = 0
    for i, row in enumerate(grid):
      max_of_rows.append(max(row))
      for j, col in enumerate(grid[i]):
        max_of_cols[j] = max(col, max_of_cols[j])
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        num = grid[i][j]
        if num < max_of_rows[i] and num < max_of_cols[j]:
          result += min(max_of_rows[i],  max_of_cols[j]) - num
    return result
