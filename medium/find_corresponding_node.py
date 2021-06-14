# Find a Corresponding Node of a Binary Tree in a Clone of That Tree

# Given two binary trees original and cloned and given a reference to a node
# target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target
# node and the answer must be a reference to a node in the cloned tree.

# Follow up: Solve the problem if repeated values on the tree are allowed.

# Example 1:

# Input: tree = [7,4,3,null,null,6,19], target = 3
# Output: 3
# Explanation: In all examples the original and cloned trees are shown. The
# target node is a green node from the original tree. The answer is the yellow
# node from the cloned tree.

from collections import deque

class Solution:
  def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    original_stack = deque([original])
    cloned_stack = deque([cloned])
    while len(original_stack):
      next_original = original_stack.popleft()
      next_cloned = cloned_stack.popleft()
      if next_original == target:
        return next_cloned
      if next_original.left:
        original_stack.append(next_original.left)
        cloned_stack.append(next_cloned.left)
      if next_original.right:
        original_stack.append(next_original.right)
        cloned_stack.append(next_cloned.right)
