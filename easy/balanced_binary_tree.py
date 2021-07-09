# Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution(object):
  def isBalanced(self, root: TreeNode):
    if root == None:
      return True
    left = self.depth(root.left)
    right = self.depth(root.right)
    return (abs(left - right) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)
  
  def depth(self,node):
    if node == None:
      return 0
    return max(self.depth(node.left),self.depth(node.right)) + 1