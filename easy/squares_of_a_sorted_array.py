# Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of
# the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Solution 1 - O(n) time, O(n) space

class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    result = []
    positive_number_index = 9999999
    negative_number_index = -999999
    for index in range(len(nums)):
      if nums[index] >= 0:
        positive_number_index = index
        break
      else:
        negative_number_index = index
    while True:
      if negative_number_index < 0 and positive_number_index >= len(nums):
        break
      elif negative_number_index >= 0 and positive_number_index < len(nums):
        squared_positive = nums[positive_number_index]**2
        squared_negative = nums[negative_number_index]**2
        if squared_positive < squared_negative:
          result.append(squared_positive)
          positive_number_index += 1
        else:
          result.append(squared_negative)
          negative_number_index -= 1
      elif negative_number_index >= 0:
        squared_negative = nums[negative_number_index]**2
        result.append(squared_negative)
        negative_number_index -= 1
      else:
        squared_positive = nums[positive_number_index]**2
        result.append(squared_positive)
        positive_number_index += 1
    return result

# Solution 2 (simplified) - O(n) time, O(n) space

class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    result = []
    left = 0
    right = len(nums) - 1
    while left <= right:
      new_left = nums[left]**2
      new_right = nums[right]**2
      if new_left > new_right:
        result.append(new_left)
        left += 1
      else:
        result.append(new_right)
        right -= 1
    return reversed(result)
