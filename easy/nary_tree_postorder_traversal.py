# N-ary Tree Postorder Traversal

# Given the root of an n-ary tree, return the postorder traversal of its nodes'
# values.

# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)

# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]

"""
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children
"""

class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    arr = []
    self.navigate(root, arr)
    return arr
    
  def navigate(self, root: 'Node', arr: List[int]) -> List[int]:
    if root is None:
      return
    for child in root.children:
      self.navigate(child, arr)
    arr.append(root.val)