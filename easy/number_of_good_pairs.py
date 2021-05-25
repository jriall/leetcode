# 1512. Number of Good Pairs

# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:
    counter = {}
    for index, num in enumerate(nums):
      if num in counter:
        counter[num].append(index)
      else:
        counter[num] = [index]
    result = 0
    for indexes in counter.values():
      count = len(indexes)
      if count > 1:
        result += count * (count - 1) // 2
    return result
