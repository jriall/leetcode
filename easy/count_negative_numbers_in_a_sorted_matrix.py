# Count Negative Numbers in a Sorted Matrix

# Given a m x n matrix grid which is sorted in non-increasing order both
# row-wise and column-wise, return the number of negative numbers in grid.

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0

class Solution:
  def countNegatives(self, grid: List[List[int]]) -> int:
    result = 0
    for row in grid:
      result += self.getNegativeNumbersInSortedList(row)
    return result

  def getNegativeNumbersInSortedList(self, arr: List[int]) -> List[int]:
    start = 0
    end = len(arr) - 1
    leftmost_negative = None
    while start <= end:
      middle = (start + end) // 2
      if arr[middle] < 0:
        leftmost_negative = middle
      if arr[middle] >= 0:
        start = middle + 1
      else:
        end = middle - 1
    return 0 if leftmost_negative is None else len(arr) - leftmost_negative
