# Sum of Unique Elements

# You are given an integer array nums. The unique elements of an array are the
# elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.

# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

class Solution:
  def sumOfUnique(self, nums: List[int]) -> int:
    hashtable = {}
    for num in nums:
      if num in hashtable:
        hashtable[num] += 1
      else:
        hashtable[num] = 1
    sum = 0
    for key, value in hashtable.items():
      if value == 1:
        sum += key
    return sum

# Follow up optimization eliminating the second loop

class Solution:
  def sumOfUnique(self, nums: List[int]) -> int:
    hashtable = {}
    count = 0
    for num in nums:
      if num in hashtable:
        hashtable[num] += 1
      if hashtable[num] == 2:
         count -= num
      else:
        hashtable[num] = 1
        count += num
    return count
