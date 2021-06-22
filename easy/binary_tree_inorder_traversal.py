# Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    result = []
    self.traverse(root, result)
    return result

  def traverse(self, root: TreeNode, arr: List[int]):
    if root is None:
      return None
    self.traverse(root.left, arr)
    arr.append(root.val)
    self.traverse(root.right, arr)
