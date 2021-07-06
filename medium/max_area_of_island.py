# Max Area of Island

# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

import collections
from dataclasses import dataclass
from typing import List

Grid = List[List[int]]

@dataclass
class Coords:
  x: int
  y: int

class Solution:
  def maxAreaOfIsland(self, grid: Grid) -> int:
    seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    biggest_island = 0
    for y in range(len(grid)):
      for x in range(len(grid[y])):
        if grid[y][x] == 1 and not seen[y][x]:
          biggest_island = max(biggest_island, self._bfs(grid, seen, Coords(x, y)))
    return biggest_island
  
  def _bfs(self, grid: Grid, seen: Grid, coords: Coords) -> int:
    island_size = 0
    stack = collections.deque([coords])
    while len(stack):
      cell = stack.popleft()
      is_in_bounds = self._is_in_bounds(grid, cell)
      if is_in_bounds and not seen[cell.y][cell.x] and grid[cell.y][cell.x] == 1:
        island_size += 1
        seen[cell.y][cell.x] = True
        stack.append(Coords(cell.x, cell.y + 1))
        stack.append(Coords(cell.x + 1, cell.y))
        stack.append(Coords(cell.x, cell.y - 1))
        stack.append(Coords(cell.x - 1, cell.y))
    return island_size

  def _is_in_bounds(self, grid: Grid, coords: Coords) -> bool:
    if coords.x < 0 or coords.y < 0:
      return False
    if coords.y >= len(grid) or coords.x >= len(grid[0]):
      return False
    return True