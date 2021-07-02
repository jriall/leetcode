# Remove Duplicates From Linked List

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    result = head
    curr = head.next
    prev = head
    while curr is not None:
      if curr.val == prev.val:
        next = curr.next
        prev.next = next
        curr = next
      else:
        prev = curr
        curr = curr.next
    return head