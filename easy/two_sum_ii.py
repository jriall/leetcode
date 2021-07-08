# Two Sum II - Input array is sorted

# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# O(n) time, O(n) space solution with hashmap

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    hashtable = {}
    for index, num in enumerate(numbers):
      target_pair = target - num
      if target_pair in hashtable:
        return [hashtable[target_pair] + 1, index + 1]
      else:
        hashtable[num] = index


# O(n) time, O(1) space solution with two pointers

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    start = 0
    end = len(numbers) - 1
    while start < end:
      total = numbers[start] + numbers[end]
      if total == target:
        return [start + 1, end + 1]
      elif total < target:
        start += 1
      else:
        end -= 1