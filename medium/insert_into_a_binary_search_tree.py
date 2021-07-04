# Insert into a Binary Search Tree

# You are given the root node of a binary search tree (BST) and a value to
# insert into the tree. Return the root node of the BST after the insertion. It
# is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.

# Example 1:

# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
      return TreeNode(val)
    curr = root
    while True:
      if val < curr.val:
        if curr.left:
          curr = curr.left
        else:
          curr.left = TreeNode(val)
          break
      else:
        if curr.right:
          curr = curr.right
        else:
          curr.right = TreeNode(val)
          break
    return root
