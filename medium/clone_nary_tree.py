# Clone N-ary Tree

# Given a root of an N-ary tree, return a deep copy (clone) of the tree.

# Each node in the n-ary tree contains a val (int) and a list (List[Node]) of
# its children.

# class Node {
#     public int val;
#     public List<Node> children;
# }
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).

# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,null,3,2,4,null,5,6]

class Solution:
  def cloneTree(self, root: 'Node') -> 'Node':
    return Node(root.val, [self.cloneTree(child) for child in root.children]) if root else None
