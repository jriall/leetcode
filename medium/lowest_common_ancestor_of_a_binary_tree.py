# Lowest Common Ancestor of a Binary Tree IV

# Given the root of a binary tree and an array of TreeNode objects nodes, return
# the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will
# exist in the tree, and all values of the tree's nodes are unique.

# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n
# nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi
# as a descendant (where we allow a node to be a descendant of itself) for every
# valid i". A descendant of a node x is a node y that is on the path from node x
# to some leaf node.

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
# Output: 2
# Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, x):
#     self.val = x
#     self.left = None
#     self.right = None

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
    if root is None:
      return None
    if root in nodes:
      return root
    left = self.lowestCommonAncestor(root.left, nodes)
    right = self.lowestCommonAncestor(root.right, nodes)
    return root if left and right else left or right