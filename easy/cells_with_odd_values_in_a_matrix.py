# Cells with Odd Values in a Matrix

# There is an m x n matrix that is initialized to all 0's. There is also a 2D
# array indices where each indices[i] = [ri, ci] represents a 0-indexed location
# to perform some increment operations on the matrix.

# For each location indices[i], do both of the following:

# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix
# after applying the increment to all locations in indices.

# Example 1:


# Input: m = 2, n = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

class Solution:
  def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
    rows = [0 for num in range(n)]
    cols = [0 for num in range(m)]
    for index in indices:
      rows[index[0]] += 1
      cols[index[1]] += 1
    result = 0
    for i in range(n):
      for j in range(m):
        if (rows[i] + cols[j]) % 2 != 0:
          result += 1
    return result