# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    counter = {}
    for num in nums:
      if num in counter:
        return True
      else:
        counter[num] = True
    return False