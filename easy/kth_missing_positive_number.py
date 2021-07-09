# Kth Missing Positive Number

# Given an array arr of positive integers sorted in a strictly increasing order,
# and an integer k.

# Find the kth positive integer that is missing from this array.

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The
# 5th missing positive integer is 9.

class Solution:
  def findKthPositive(self, arr: List[int], k: int) -> int:
    i = 0
    curr = 0
    while k > 0:
      curr += 1
      if i < len(arr) and arr[i] == curr:
        i += 1
      else:
        k -= 1
    return curr
      