# Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root
# node down to the nearest leaf node.

# Note: A leaf is a node with no children.

import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def minDepth(self, root: TreeNode) -> int:
    if root is None:
      return 0
    stack = [(root, 0)]
    min_depth = math.inf
    while len(stack):
      value, depth = stack.pop()
      new_depth = depth + 1
      if value.left is None and value.right is None:
        min_depth = new_depth if new_depth < min_depth else min_depth
      if value.left is not None:
        stack.append((value.left, new_depth))
      if value.right is not None:
        stack.append((value.right, new_depth))
    return min_depth