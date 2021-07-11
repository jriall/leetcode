# Minimum Absolute Difference in BST

# Given the root of a Binary Search Tree (BST), return the minimum absolute
# difference between the values of any two different nodes in the tree.

# Example 1:

# Input: root = [4,2,6,1,3]
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def getMinimumDifference(self, root: TreeNode) -> int:
    arr = []
    self.in_order_traversal(root, arr)
    smallest_difference = float('inf')
    for i in range(len(arr) - 1):
      smallest_difference = min(smallest_difference, arr[i + 1] - arr[i])
    return smallest_difference
    
  def in_order_traversal(self, root: TreeNode, arr: List[int]):
    if root is None:
      return None
    self.in_order_traversal(root.left, arr)
    arr.append(root.val)
    self.in_order_traversal(root.right, arr)
    