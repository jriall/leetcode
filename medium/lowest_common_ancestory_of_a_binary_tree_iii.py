# Lowest Common Ancestor of a Binary Tree III

# Given two nodes of a binary tree p and q, return their lowest common ancestor
# (LCA).

# Each node will have a reference to its parent node. The definition for Node is
# below:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor
# of two nodes p and q in a tree T is the lowest node that has both p and q as
# descendants (where we allow a node to be a descendant of itself)."

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

"""
# Definition for a Node.
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
"""
class Solution:
  def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    root = p
    while root.parent:
      root = root.parent
    depth_p = self.get_depth(p)
    depth_q = self.get_depth(q)
    diff = abs(depth_p - depth_q)
    p_is_deeper = True if depth_p > depth_q else False
    if diff > 0:
      while diff > 0:
        if p_is_deeper:
          p = p.parent
        else:
          q = q.parent
        diff -= 1
    while q is not p:
      p = p.parent
      q = q.parent
    return p
      
    
  def get_depth(self, node: 'Node') -> int:
    level = 1
    curr = node
    while curr.parent:
      level += 1
      curr = curr.parent
    return level