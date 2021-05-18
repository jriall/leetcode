# Range Sum of BST

# Given the root node of a binary search tree and two integers low and high,'
# return the sum of values of all nodes with a value in the inclusive range
# [low, high].

class Solution:
  def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    count = []
    self.tree_walker(root, low, high, count)
    return sum(count)
  
  def tree_walker(self, root: TreeNode, low: int, high: int, count: List[int]):
    if low <= root.val <= high:
        count.append(root.val)
    if root.left is not None:
        self.tree_walker(root.left, low, high, count)
    if root.right is not None:
        self.tree_walker(root.right, low, high, count)

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# Improved recursive solution

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    if root is None:
      return 0
    count = 0
    if low <= root.val <= high:
      count += root.val
    if root.left is not None:
      count += self.rangeSumBST(root.left, low, high)
    if root.right is not None:
      count += self.rangeSumBST(root.right, low, high)
    return count