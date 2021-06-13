# Binary Tree Preorder Traversal

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def preorderTraversal(self, root: TreeNode) -> List[int]:
    arr = []
    self.traverse(root, arr)
    return arr

  def traverse(self, root: TreeNode, arr: List[int]):
    if root is None:
      return
    arr.append(root.val)
    self.traverse(root.left, arr)
    self.traverse(root.right, arr)
