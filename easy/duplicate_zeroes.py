# Duplicate Zeros

# Given a fixed length array arr of integers, duplicate each occurrence of zero,
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.

# Do the above modifications to the input array in place, do not return anything
# from your function.

# Example 1:

# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,0,0,2,3,0,0,4]

class Solution:
  def duplicateZeros(self, arr: List[int]) -> None:
    index = 0
    while index < len(arr) -1:
      if arr[index] == 0:
        arr.insert(index + 1, 0)
        arr.pop()
        index += 2
      else: index += 1