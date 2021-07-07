# Find Leaves of Binary Tree

# Given the root of a binary tree, collect a tree's nodes as if you were doing
# this:

# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.

# Example 1:

# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]
# Explanation:
# [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers
# since per each level it does not matter the order on which elements are
# returned.

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def findLeaves(self, root: TreeNode) -> List[List[int]]:
    results = []
    while root.left or root.right:
      result = []
      self.traverse(root, result)
      results.append(result)
    results.append([root.val])
    return results
    
  def traverse(self, root: TreeNode, result: List[int]):
    if not root:
      return
    if root.left:
      if not root.left.left and not root.left.right:
        result.append(root.left.val)
        root.left = None
    if root.right:
      if not root.right.left and not root.right.right:
        result.append(root.right.val)
        root.right = None
    self.traverse(root.left, result)
    self.traverse(root.right, result)