# Maximum Level Sum of a Binary Tree

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def maxLevelSum(self, root: TreeNode) -> int:
    levels = self.bfs(root)
    max_val = float('-inf')
    level = 0
    for key, value in levels.items():
      if value > max_val:
        level = key
        max_val = value
    return level
    
  def bfs(self, root: TreeNode):
    levels = {}
    stack = [(root, 1)]
    while len(stack):
      next_node, level = stack.pop(0)
      if level in levels:
        levels[level] += next_node.val 
      else:
        levels[level] = next_node.val
      if next_node.left is not None:
        stack.append((next_node.left, level + 1))
      if next_node.right is not None:
        stack.append((next_node.right, level + 1))
    return levels
    
    