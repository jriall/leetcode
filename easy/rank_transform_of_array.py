# Rank Transform of an Array

# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following
# rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their
# rank must be the same.
# Rank should be as small as possible.

# Example 1:

# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second
# smallest. 30 is the third smallest.

class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    sorted_arr = sorted(arr)
    ranks = {}
    rank = 1
    for num in sorted_arr:
      if num not in ranks:
        ranks[num] = rank
        rank += 1
    return [ranks[num] for num in arr]
