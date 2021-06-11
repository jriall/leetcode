# Monotonic Array

# An array is monotonic if it is either monotone increasing or monotone
# decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Return true if and only if the given array nums is monotonic.

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true

class Solution:
  def isMonotonic(self, nums: List[int]) -> bool:
    if len(nums) <= 2:
      return True
    is_increasing = None
    for i in range(1, len(nums)):
      if nums[i] > nums[i-1]:
        if is_increasing == False:
          return False
        is_increasing = True
      elif nums[i] < nums[i-1]:
        if is_increasing == True:
          return False
        is_increasing = False
    return True