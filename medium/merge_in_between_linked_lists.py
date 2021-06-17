# Merge In Between Linked Lists

# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their
# place.

# The blue edges and nodes in the following figure incidate the result:

# Build the result list and return its head.

# Example 1:

# Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [0,1,2,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their
# place. The blue edges and nodes in the above figure indicate the result.

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    first = list1
    second = list1
    a -= 1
    b += 1
    while True:
      if a > 0:
        first = first.next
        a -= 1
      if b > 0:
        second = second.next
        b -= 1
      if a == 0 and b == 0:
        break
    first.next = list2
    while first.next is not None:
      first = first.next
    first.next = second
    return list1
