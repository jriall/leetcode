# Swapping Nodes in a Linked List

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node
# from the beginning and the kth node from the end (the list is 1-indexed).

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def swapNodes(self, head: ListNode, k: int) -> ListNode:
    count = 0
    curr = head
    kth_node_from_start = None
    kth_node_from_end = None
    while curr is not None:
      count += 1
      if count == k:
        kth_node_from_start = curr
        kth_node_from_end = head
      if count > k:
        kth_node_from_end = kth_node_from_end.next
      curr = curr.next
    temp = kth_node_from_start.val
    kth_node_from_start.val = kth_node_from_end.val
    kth_node_from_end.val = temp
    return head