# Closest Binary Search Tree Value

# Given the root of a binary search tree and a target value, return the value in
# the BST that is closest to the target.

# Example 1:

# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def closestValue(self, root: TreeNode, target: float) -> int:
    current_node = root
    closest_so_far = root.val
    while current_node:
      if abs(current_node.val - target) < abs(closest_so_far - target):
        closest_so_far = current_node.val
      if closest_so_far == round(target):
        break
      if target < current_node.val:
        current_node = current_node.left
      else:
        current_node = current_node.right
    return closest_so_far