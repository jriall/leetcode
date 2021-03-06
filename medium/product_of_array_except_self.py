# Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.

# You must write an algorithm that runs in O(n) time and without using the
# division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    result = [1 for _ in nums]
    left_count = 1
    for i in range(1, len(nums)):
      left_count *= nums[i - 1]
      result[i] = left_count
    right_count = 1
    for i in reversed(range(len(nums) -1)):
      right_count *= nums[i + 1]
      result[i] = right_count * result[i]
    return result
