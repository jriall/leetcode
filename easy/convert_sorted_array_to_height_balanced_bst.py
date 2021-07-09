# Convert Sorted Array to Binary Search Tree

# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two
# subtrees of every node never differs by more than one.

# Example 1:

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

from typing import List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if len(nums) == 0:
      return None
    middle = len(nums) // 2
    root = TreeNode(nums[middle])
    root.left = self.sortedArrayToBST(nums[:middle])
    root.right = self.sortedArrayToBST(nums[middle + 1:])
    return root
