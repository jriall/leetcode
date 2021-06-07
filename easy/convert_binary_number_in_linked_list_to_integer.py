# Convert Binary Number in a Linked List to Integer

# Given head which is a reference node to a singly-linked list. The value of
# each node in the linked list is either 0 or 1. The linked list holds the
# binary representation of a number.

# Return the decimal value of the number in the linked list.

# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def getDecimalValue(self, head: ListNode) -> int:
    binary_num = []
    curr = head
    while curr:
      binary_num.append(str(curr.val))
      curr = curr.next
    return int(''.join(binary_num), 2)
