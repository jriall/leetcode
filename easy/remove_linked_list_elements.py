# Remove Linked List Elements

# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.

# Example 1:

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    result = head
    while result and result.val == val:
      result = result.next
    curr = result
    while curr and curr.next is not None:
      if curr.next.val == val:
        curr.next = curr.next.next
      else: 
        curr = curr.next
    return result