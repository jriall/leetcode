# Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index
# if the target is found. If not, return the index where it would be if it were
# inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    if target > nums[-1]:
      return len(nums)
    elif target <= nums[0]:
      return 0
    start_index = 0
    end_index = len(nums)
    while start_index < end_index:
      middle_index = (start_index + end_index)//2
      if nums[middle_index] == target:
        return middle_index
      elif nums[middle_index] > target:
        end_index = middle_index
      else:
        start_index = middle_index + 1
    return start_index
