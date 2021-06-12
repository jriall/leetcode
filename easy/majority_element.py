# Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# O(n) time, O(n) space solution

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    count = {}
    for num in nums:
      if num in count:
        count[num] += 1
      else:
        count[num] = 1
      if count[num] > len(nums) / 2:
        return num

# O(n) time, O(1) space solution using majority vote algorithm

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    candidate = None
    count = 0
    for num in nums:
      if candidate is None:
        candidate = num
        count = 1
      elif num == candidate:
        count += 1
      elif num != candidate:
        count -= 1
        if count == 0:
          candidate = None
    return candidate