# Same Tree

# Given the roots of two binary trees p and q, write a function to check if they
# are the same or not.

# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
from collections import deque

class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    p_arr = []
    q_arr = []
    self.traverse(p, p_arr)
    self.traverse(q, q_arr)
    print(p_arr, q_arr)
    return p_arr == q_arr


  def traverse(self, node: TreeNode, arr: List[int]):
    if node:
      arr.append(node.val)
      self.traverse(node.left, arr)
      self.traverse(node.right, arr)
    else:
      arr.append(None)
