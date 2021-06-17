# Sum of Nodes with Even-Valued Grandparent

# Given a binary tree, return the sum of values of nodes with even-valued
# grandparent.  (A grandparent of a node is the parent of its parent, if it
# exists.)

# If there are no nodes with an even-valued grandparent, return 0.

# Example 1:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the
# blue nodes are the even-value grandparents.

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def sumEvenGrandparent(self, root: TreeNode) -> int:
    result = []
    self.traverse(root, result)
    return sum(result)
  
  def traverse(self,
               root: TreeNode,
               result: List[int],
               parent: Optional[TreeNode] = None,
               grandparent: Optional[TreeNode] = None):
    if root is None:
      return
    if grandparent and grandparent.val % 2 == 0:
      result.append(root.val)
    new_parent = root
    new_grandparent = parent
    self.traverse(root.left, result, new_parent, new_grandparent)
    self.traverse(root.right, result, new_parent, new_grandparent)
