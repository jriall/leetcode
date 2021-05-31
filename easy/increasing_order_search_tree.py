# Increasing Order Search Tree

# Given the root of a binary search tree, rearrange the tree in in-order so that
# the leftmost node in the tree is now the root of the tree, and every node has
# no left child and only one right child.

# Example 1:

# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def increasingBST(self, root: TreeNode) -> TreeNode:
    arr = []
    self.inOrderTraversal(root, arr)
    head = TreeNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
      new_node = TreeNode(arr[i])
      curr.right = new_node
      curr = new_node
    return head
    
    
  def inOrderTraversal(self, node, arr):
    if node is None:
      return
    self.inOrderTraversal(node.left, arr)
    arr.append(node.val)
    self.inOrderTraversal(node.right, arr)
    
    