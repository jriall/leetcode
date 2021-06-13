# Binary Tree Postorder Traversal

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def postorderTraversal(self, root: TreeNode) -> List[int]:
    arr = []
    self.traverse(root, arr)
    return arr

  def traverse(self, root: TreeNode, arr: List[int]):
    if root is None:
      return
    self.traverse(root.left, arr)
    self.traverse(root.right, arr)
    arr.append(root.val)