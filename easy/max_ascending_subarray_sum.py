# Maximum Ascending Subarray Sum

# Given an array of positive integers nums, return the maximum possible sum of
# an ascending subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.

# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
# where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.

# Example 1:

# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

class Solution:
  def maxAscendingSum(self, nums: List[int]) -> int:
    biggest_subarray_sum = nums[0]
    current_sum = nums[0]
    index = 1
    while index < len(nums):
      if nums[index] > nums[index - 1]:
        current_sum += nums[index]
        biggest_subarray_sum = max(biggest_subarray_sum, current_sum)
      else:
        current_sum = nums[index]
      index += 1
    return biggest_subarray_sum
      