# Deepest Leaves Sum

# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Example 1:

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

# Recursive traversal solution

class Solution:
  def deepestLeavesSum(self, root: TreeNode) -> int:
    target_depth = self.get_depth(root, 0)
    deepest_nodes = []
    self.get_sum_of_deepest(root, target_depth, 1, deepest_nodes)
    return sum(deepest_nodes)

  def get_depth(self, root: TreeNode, sum: int):
    if root is None:
      return 0
    max_left = self.get_depth(root.left, sum)
    max_right = self.get_depth(root.right, sum)
    return max(max_left, max_right) + 1

  def get_sum_of_deepest(self, root: TreeNode, target_depth: int, current_depth: int, deepest_nodes: List[int]):
    if root is None:
      return
    if current_depth == target_depth:
      deepest_nodes.append(root.val)
    else:
      new_depth = current_depth + 1
      self.get_sum_of_deepest(root.left, target_depth, new_depth, deepest_nodes)
      self.get_sum_of_deepest(root.right, target_depth, new_depth, deepest_nodes)

# Stack level traversal solution

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def deepestLeavesSum(self, root: TreeNode) -> int:
    stack = [root]
    while True:
      lefts = [node.left for node in stack if node.left]
      rights = [node.right for node in stack if node.right]
      next = lefts + rights
      if len([node for node in next]) == 0:
        break
      stack = next
      return sum([node.val for node in stack])
