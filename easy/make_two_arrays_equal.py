# Make Two Arrays Equal by Reversing Sub-arrays

# Given two integer arrays of equal length target and arr.

# In one step, you can select any non-empty sub-array of arr and reverse it. You
# are allowed to make any number of steps.

# Return True if you can make arr equal to target, or False otherwise.

# Example 1:

# Input: target = [1,2,3,4], arr = [2,4,1,3]
# Output: true
# Explanation: You can follow the next steps to convert arr to target:
# 1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
# 2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
# 3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
# There are multiple ways to convert arr to target, this is not the only way to
# do so.

class Solution:
  def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    target_vals = {}
    for val in target:
      if val in target_vals:
        target_vals[val] += 1
      else:
        target_vals[val] = 1
    for val in arr:
      if val not in target_vals:
        return False
      target_vals[val] -= 1
      if target_vals[val] == 0:
        del target_vals[val]
    return len(target_vals.keys()) == 0
