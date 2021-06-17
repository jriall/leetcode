# All Elements in Two Binary Search Trees

# Given two binary search trees root1 and root2.

# Return a list containing all the integers from both trees sorted in ascending order.

# Example 1:

# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:

# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
# Output: [-10,0,0,1,2,5,7,10]

# Definition for a binary tree node.
# class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right
class Solution:
   def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
      nodes1 = []
      self.inOrderTraversal(root1, nodes1)
      nodes2 = []
      self.inOrderTraversal(root2, nodes2)
      return self.combineTwoSortedLists(nodes1, nodes2)

   def inOrderTraversal(self, root: TreeNode, arr: List[int]):
      if root is None:
         return
      self.inOrderTraversal(root.left, arr)
      arr.append(root.val)
      self.inOrderTraversal(root.right, arr)

   def combineTwoSortedLists(self, list1: List[int], list2: List[int]) -> List[int]:
      result = []
      pointer1 = 0
      pointer2 = 0
      while pointer1 < len(list1) or pointer2 < len(list2):
         if pointer1 >= len(list1):
            result.append(list2[pointer2])
            pointer2 += 1
         elif pointer2 >= len(list2):
            result.append(list1[pointer1])
            pointer1 += 1
         elif list1[pointer1] < list2[pointer2]:
            result.append(list1[pointer1])
            pointer1 += 1
         else:
            result.append(list2[pointer2])
            pointer2 += 1
      return result
