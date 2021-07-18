# Peak Index in a Mountain Array

# Let's call an array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i
# such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# Example 1:

# Input: arr = [0,1,0]
# Output: 1

class Solution:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
      middle = (start + end) // 2
      if arr[middle - 1] < arr[middle] > arr[middle + 1]:
        return middle
      elif arr[middle] > arr[middle + 1]:
        end = middle - 1
      else:
        start = middle + 1