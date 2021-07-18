# Correct a Binary Tree

# You have a binary tree with a small defect. There is exactly one invalid node
# where its right child incorrectly points to another node at the same depth but
# to the invalid node's right.

# Given the root of the binary tree with this defect, root, return the root of
# the binary tree after removing this invalid node and every node underneath it
# (minus the node it incorrectly points to).

# Custom testing:

# The test input is read as 3 lines:

# TreeNode root
# int fromNode (not available to correctBinaryTree)
# int toNode (not available to correctBinaryTree)
# After the binary tree rooted at root is parsed, the TreeNode with value of
# fromNode will have its right child pointer pointing to the TreeNode with a
# value of toNode. Then, root is passed to correctBinaryTree.

# Example 1:

# Input: root = [1,2,3], fromNode = 2, toNode = 3
# Output: [1,null,3]
# Explanation: The node with value 2 is invalid, so remove it.

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def correctBinaryTree(self, root: TreeNode) -> TreeNode:
    queue = [(root, None)]
    seen = {}
    for node, prev in queue:
      if node.right and node.right.val in seen:
        if node == prev.left:
          prev.left = None
        if node == prev.right:
          prev.right = None
        return root
      seen[node.val] = True
      if node.right:
        queue.append((node.right, node))
      if node.left:
        queue.append((node.left, node))
