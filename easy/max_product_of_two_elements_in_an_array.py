# Maximum Product of Two Elements in an Array

# Given the array of integers nums, you will choose two different indices i and
# j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you
# will get the maximum value, that is,
# (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

# Example 2:

# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get
# the maximum value of (5-1)*(5-1) = 16.
# Example 3:

# Input: nums = [3,7]
# Output: 12

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    if len(nums) == 2:
      return (nums[0]-1)*(nums[1]-1)
    biggest_index = 0 if nums[0] >= nums[1] else 1
    second_biggest_index = 1 if biggest_index == 0 else 0
    for index in range(2, len(nums)):
      if nums[index] >= nums[biggest_index]:
        second_biggest_index = biggest_index
        biggest_index = index
      elif nums[index] > nums[second_biggest_index]:
        second_biggest_index = index
    return (nums[biggest_index]-1)*(nums[second_biggest_index]-1)