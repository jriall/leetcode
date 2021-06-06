# Binary Search

# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
      middle = (start + end) // 2
      if nums[middle] == target:
        return middle
      elif target < nums[middle]:
        end = middle - 1
      else:
        start = middle + 1
    return -1
