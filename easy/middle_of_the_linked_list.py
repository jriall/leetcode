# Middle of the Linked List

# Given a non-empty, singly linked list with head node head, return a middle
# node of linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is
# [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and
# ans.next.next.next = NULL.

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    nodes = 0
    curr = head
    while curr is not None:
      nodes += 1
      curr = curr.next
    target_node = nodes // 2 + 1
    curr = head
    count = 1
    while True:
      if count == target_node:
        return curr
      else: 
        curr = curr.next
        count += 1