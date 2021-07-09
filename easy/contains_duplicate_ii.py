# Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and
# abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# O(n) time, O(n) space.
class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    hashmap = {}
    for index, num in enumerate(nums):
      if num in hashmap and abs(index - hashmap[num]) <= k:
        return True
      hashmap[num] = index
    return False

