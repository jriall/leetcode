# Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must appear as many times as it shows
# in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    count = {}
    for num in nums1:
      if num in count:
        count[num] += 1
      else:
        count[num] = 1
    result = []
    for num in nums2:
      if count.get(num, 0) > 0:
        result.append(num)
        count[num] -= 1
    return result