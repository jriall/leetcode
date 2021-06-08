# Unique Number of Occurrences

# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values
# have the same number of occurrences.

class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    occurances = {}
    for num in arr:
      if num in occurances:
        occurances[num] += 1
      else:
        occurances[num] = 1
    unique_occurances = {}
    for occurance in occurances.values():
      if occurance in unique_occurances:
        return False
      else:
        unique_occurances[occurance] = True
    return True
