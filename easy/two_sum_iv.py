# Two Sum IV - Input is a BST

# Given the root of a Binary Search Tree and a target number k, return true if
# there exist two elements in the BST such that their sum is equal to the given
# target.

# Example 1:

# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  
  def __init__(self):
    self._hashtable = {}
    self._seen = False
  
  def findTarget(self, root: TreeNode, k: int) -> bool:
    self.traverse(root, k)
    return self._seen

  def traverse(self, root: TreeNode, k: int):
    if root is None:
      return
    self.traverse(root.left, k)
    target = k - root.val
    if target in self._hashtable:
      self._seen = True
    self._hashtable[root.val] = True
    self.traverse(root.right, k)

# Simpler solution using DFS
class Solution: 
  def findTarget(self, root: TreeNode, k: int) -> bool:
    stack = [root]
    seen = {}
    while len(stack):
      next = stack.pop(0)
      target = k - next.val
      if target in seen:
        return True
      seen[next.val] = True
      if next.left:
        stack.append(next.left)
      if next.right:
        stack.append(next.right)
    return False