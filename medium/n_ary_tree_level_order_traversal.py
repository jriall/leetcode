# N-ary Tree Level Order Traversal

# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).

# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]

"""
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children
"""

class Solution:
  def levelOrder(self, root: 'Node') -> List[List[int]]:
    results = []
    if root is None:
      return results
    stack = [(root, 0)]
    while len(stack):
      next_node, level = stack.pop(0)
      for child in next_node.children:
        stack.append((child, level + 1))
      if level < len(results):
        results[level].append(next_node.val)
      else:
        results.append([next_node.val])
    return results