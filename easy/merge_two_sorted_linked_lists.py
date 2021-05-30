# Merge two sorted linked lists

# Merge two sorted linked lists and return it as a sorted list. The list should
# be made by splicing together the nodes of the first two lists.

# Example 1:

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: l1 = [], l2 = []
# Output: []
# Example 3:

# Input: l1 = [], l2 = [0]

# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
      return l2
    if l2 is None:
      return l1
    curr1 = l1
    curr2 = l2
    new_head = ListNode()
    if curr1.val < curr2.val:
      new_head.val = curr1.val
      curr1 = curr1.next
    else:
      new_head.val = curr2.val
      curr2 = curr2.next
    curr = new_head
    while True:
      if curr1 is None and curr2 is None:
        return new_head
      elif curr1 is None:
        curr.next = ListNode(curr2.val)
        curr2 = curr2.next
      elif curr2 is None:
        curr.next = ListNode(curr1.val)
        curr1 = curr1.next
      else:
        if curr1.val < curr2.val:
          curr.next = ListNode(curr1.val)
          curr1 = curr1.next
        else:
          curr.next = ListNode(curr2.val)
          curr2 = curr2.next
      curr = curr.next
