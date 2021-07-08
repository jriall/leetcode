# Remove Duplicates from Sorted List II

# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.

# Example 1:

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:

# Input: head = [1,1,1,2,3]
# Output: [2,3]

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head or not head.next:
      return head
    vals = []
    curr = head
    while curr:
      vals.append(curr.val)
      curr = curr.next
    unique_numbers = []
    for i in range(len(vals)):
      if i == 0 and vals[i] != vals[i + 1]:
        unique_numbers.append(vals[i])
      elif i == len(vals) - 1 and vals[i] != vals[i - 1]:
        unique_numbers.append(vals[i])
      elif vals[i] != vals[i - 1] and vals[i] != vals[i + 1]:
        unique_numbers.append(vals[i])
    if len(unique_numbers) == 0:
      return None
    result = ListNode(unique_numbers[0])
    curr = result
    i = 1
    while i < len(unique_numbers):
      curr.next = ListNode(unique_numbers[i])
      curr = curr.next
      i += 1
    return result