# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.

# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l1_length = 0
    l2_length = 0
    curr1 = l1
    curr2 = l2
    carry_over = 0
    while curr1 or curr2:
      new_val = carry_over
      if curr1:
        new_val += curr1.val
      if curr2:
        new_val += curr2.val
      if curr1:
        curr1.val = new_val % 10
      carry_over = 0 if new_val < 10 else 1
      if curr1:
        curr1.val = new_val % 10
        l1_length += 1
        curr1 = curr1.next
      if curr2:
        curr2.val = new_val % 10
        l2_length += 1
        curr2 = curr2.next
    longest_list = l1 if l1_length >= l2_length else l2
    if carry_over:
      curr = longest_list
      while curr.next:
        curr = curr.next
      curr.next = ListNode(1)
    return longest_list