# Intersection of Two Linked Lists

# Given the heads of two singly linked-lists headA and headB, return the node at
# which the two lists intersect. If the two linked lists have no intersection at
# all, return null.

# For example, the following two linked lists begin to intersect at node c1:


# It is guaranteed that there are no cycles anywhere in the entire linked
# structure.

# Note that the linked lists must retain their original structure after the
# function returns.

# Example 1:

# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5],
# skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as
# [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3
# nodes before the intersected node in B.

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    depthA = self.getListLength(headA)
    depthB = self.getListLength(headB)
    currA = headA
    currB = headB
    while depthA != depthB:
      if depthA > depthB:
        currA = currA.next
        depthA -= 1
      else:
        currB = currB.next
        depthB -= 1
    while currA != currB:
      currA = currA.next
      currB = currB.next
    return currA

  def getListLength(self, head: ListNode) -> int:
    depth = 0
    curr = head
    while curr:
      depth += 1
      curr = curr.next
    return depth