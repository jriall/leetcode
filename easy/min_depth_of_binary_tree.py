# Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root
# node down to the nearest leaf node.

# Note: A leaf is a node with no children.

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
    left_subtree = self.minDepth(root.left)
    right_subtree = self.minDepth(root.right)
    return 1 + min([left_subtree, right_subtree])
