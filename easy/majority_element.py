# Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    count = {}
    for num in nums:
      if num in count:
        count[num] += 1
      else:
        count[num] = 1
    result = None
    biggest = 0
    for key, value in count.items():
      if value > biggest:
        result = key
        biggest = value
    return result
      