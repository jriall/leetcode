# N-Repeated Element in Size 2N Array

# In a array nums of size 2 * n, there are n + 1 unique elements, and exactly one of these elements is repeated n times.

# Return the element repeated n times.

class Solution:
  def repeatedNTimes(self, nums: List[int]) -> int:
    n = len(nums) / 2
    counter = {}
    for num in nums:
      if num in counter:
        counter[num] += 1
      else:
        counter[num] = 1
    for key, value in counter.items():
      if value == n:
        return key
