# Find Smallest Common Element in All Rows

# Given an m x n matrix mat where every row is sorted in strictly increasing
# order, return the smallest common element in all rows.

# If there is no common element, return -1.

# Example 1:
# Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
# Output: 5

# Example 2:
# Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
# Output: 2

# O(rc) time, O(r) space 
class Solution:
  def smallestCommonElement(self, mat: List[List[int]]) -> int:
    possible_results = {}
    biggest = float('-inf')
    for num in mat[0]:
      possible_results[num] = True
      biggest = max(biggest, num)
    for i in range(1, len(mat)):
      for j in range(len(mat[0])):
        if mat[i][j] > biggest:
          break
        if mat[i][j] in possible_results:
          possible_results[mat[i][j]] += 1
    for key, value in possible_results.items():
      if value == len(mat):
        return key
    return -1
        
      