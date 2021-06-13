# Element Appearing More Than 25% In Sorted Array

# Given an integer array sorted in non-decreasing order, there is exactly one
# integer in the array that occurs more than 25% of the time, return that
# integer.

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6

class Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
    current_count = 1
    for i in range(1, len(arr)):
      if arr[i] == arr[i-1]:
        current_count += 1
        if current_count > len(arr) / 4:
          return arr[i]
      else:
        current_count = 1