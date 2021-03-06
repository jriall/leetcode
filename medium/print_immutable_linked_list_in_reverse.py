# Print Immutable Linked List in Reverse

# You are given an immutable linked list, print out all values of each node in
# reverse with the help of the following interface:

# ImmutableListNode: An interface of immutable linked list, you are given the
# head of the list.
# You need to use the following functions to access the linked list (you can't
# access the ImmutableListNode directly):

# ImmutableListNode.printValue(): Print value of the current node.
# ImmutableListNode.getNext(): Return the next node.
# The input is only given to initialize the linked list internally. You must
# solve this problem without modifying the linked list. In other words, you must
# operate the linked list using only the mentioned APIs.

# Example 1:

# Input: head = [1,2,3,4]
# Output: [4,3,2,1]

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#   def printValue(self) -> None: # print the value of this node.
#   def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
  def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
    nodes = []
    curr = head
    while curr:
      nodes.append(curr)
      curr = curr.getNext()
    for i in reversed(range(len(nodes))):
      nodes[i].printValue()

# Recursive solution

def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
  if head.getNext():
    self.printLinkedListInReverse(head.getNext())
  head.printValue()
