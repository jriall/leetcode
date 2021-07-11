# Sum of Left Leaves

# Given the root of a binary tree, return the sum of all left leaves.

# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and
# 15 respectively.

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def __init__(self):
    self.result = 0

  def sumOfLeftLeaves(self, root: TreeNode) -> int:
    self.traverse(root)
    return self.result
    
  def traverse(self, root: TreeNode):
    if root is None:
      return
    if root.left and root.left.left is None and root.left.right is None:
      self.result += root.left.val
    self.traverse(root.left)
    self.traverse(root.right)
