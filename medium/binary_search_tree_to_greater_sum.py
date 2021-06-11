# Binary Search Tree to Greater Sum Tree

# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
# such that every key of the original BST is changed to the original key plus
# sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these
# constraints:

# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:

# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def bstToGst(self, root: TreeNode) -> TreeNode:
    nodes = []
    self.search(root, nodes)
    self.increase_nodes(root, nodes)
    return root

  def search(self, root: TreeNode, nodes: List[int]):
    if root is None:
      return
    self.search(root.right, nodes)
    nodes.append(root.val)
    self.search(root.left, nodes)
  
  def increase_nodes(self, root: TreeNode, nodes: List[int]):
    if root is None:
      return
    self.increase_nodes(root.left, nodes)
    root.val = sum(nodes)
    nodes.pop()
    self.increase_nodes(root.right, nodes)

# Improved solution only traversing the tree once

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def bstToGst(self, root: TreeNode) -> TreeNode:
    self.sum = 0
    self.increase_nodes(root)
    return root

  def increase_nodes(self, root: TreeNode):
    if root is None:
      return
    self.increase_nodes(root.right)
    self.sum += root.val
    root.val = self.sum
    self.increase_nodes(root.left)