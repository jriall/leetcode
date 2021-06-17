# Balance a Binary Search Tree

# Given a binary search tree, return a balanced binary search tree with the same
# node values.

# A binary search tree is balanced if and only if the depth of the two subtrees
# of every node never differ by more than 1.

# If there is more than one answer, return any of them.

# Example 1:

# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is
# also correct.

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def balanceBST(self, root: TreeNode) -> TreeNode:
    vals = []
    self.in_order_traversal(root, vals)
    return self.create_bst_from_vals(vals)

  def in_order_traversal(self, root: TreeNode, vals: List[int]):
    if root is None:
      return
    self.in_order_traversal(root.left, vals)
    vals.append(root.val)
    self.in_order_traversal(root.right, vals)

  def create_bst_from_vals(self, vals: List[int]) -> TreeNode:
    if len(vals) == 0:
      return None
    middle_index = len(vals) // 2
    return TreeNode(
      val=vals[middle_index],
      left=self.create_bst_from_vals(vals[0:middle_index]),
      right=self.create_bst_from_vals(vals[middle_index+1:]),
    )
