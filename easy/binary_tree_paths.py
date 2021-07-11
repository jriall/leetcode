# Binary Tree Paths

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Example 1:

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def binaryTreePaths(self, root):
    results = []
    self.navigate(root, results)
    return results
    
  def navigate(self, root, arr, path = []):
    if root is None:
      return
    new_path = path.copy() + [root.val]
    if root.left is None and root.right is None:
      arr.append('->'.join([str(val) for val in new_path]))
    self.navigate(root.left, arr, new_path)
    self.navigate(root.right, arr, new_path)