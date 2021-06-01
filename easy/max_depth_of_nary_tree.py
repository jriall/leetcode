# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the
# root node down to the farthest leaf node.

# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).

# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3

"""
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children
"""

class Solution:
  def maxDepth(self, root: 'Node') -> int:
    if root is None:
      return 0
    child_depths = []
    for child in root.children:
      child_depths.append(self.maxDepth(child))
    return max(child_depths) + 1 if len(child_depths) else 1
    