# Average of Levels in Binary Tree

# Given the root of a binary tree, return the average value of the nodes on each
# level in the form of an array. Answers within 10-5 of the actual answer will
# be accepted.

# Example 1:

# Input: root = [3,9,20,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def averageOfLevels(self, root: TreeNode) -> List[float]:
    stack = [(root, 1)]
    levels = {}
    biggest_level = 1
    while len(stack):
      node, level = stack.pop(0)
      if level in levels:
        levels[level].append(node.val)
      else:
        levels[level] = [node.val]
      if node.right:
        stack.append((node.right, level + 1))
      if node.left:
        stack.append((node.left, level + 1))
      biggest_level = max(biggest_level, level)
    results = [0 for _ in range(biggest_level)]
    for key, value in levels.items():
      results[key - 1] = sum(value) / len(value)
    return results