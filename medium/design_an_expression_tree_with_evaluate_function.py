# Design an Expression Tree With Evaluate Function

# Given the postfix tokens of an arithmetic expression, build and return the
# binary expression tree that represents this expression.

# Postfix notation is a notation for writing arithmetic expressions in which the
# operands (numbers) appear before their operators. For example, the postfix
# tokens of the expression 4*(5-(7+2)) are represented in the array postfix =
# ["4","5","7","2","+","-","*"].

# The class Node is an interface you should use to implement the binary
# expression tree. The returned tree will be tested using the evaluate function,
# which is supposed to evaluate the tree's value. You should not remove the Node
# class; however, you can modify it as you wish, and you can define other
# classes to implement it if needed.

# A binary expression tree is a kind of binary tree used to represent arithmetic
# expressions. Each node of a binary expression tree has either zero or two
# children. Leaf nodes (nodes with 0 children) correspond to operands (numbers),
# and internal nodes (nodes with two children) correspond to the operators '+'
# (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

# It's guaranteed that no subtree will yield a value that exceeds 109 in
# absolute value, and all the operations are valid (i.e., no division by zero).

# Follow up: Could you design the expression tree such that it is more modular?
# For example, is your design able to support additional operators without
# making changes to your existing evaluate implementation?

 

# Example 1:



# Input: s = ["3","4","+","2","*","7","/"]
# Output: 2
# Explanation: this expression evaluates to the above binary tree with
# expression ((3+4)*2)/7) = 14/7 = 2.

from typing import Dict, List, Optional
from abc import ABC, abstractmethod 


class Node(ABC):
  @abstractmethod
  def evaluate(self) -> int:
    pass


class OperatorNode:
  def __init__(self, left: Optional[Node], right: Optional[Node]):
    self.left = left
    self.right = right


class AddNode(Node, OperatorNode):
  def __init__(self, left: Optional[Node] = None, right: Optional[Node] = None):
    OperatorNode.__init__(self, left, right)
    
  def evaluate(self) -> int:
    return int(self.left.evaluate() + self.right.evaluate())


class DivideNode(Node, OperatorNode):
  def __init__(self, left: Optional[Node] = None, right: Optional[Node] = None):
    OperatorNode.__init__(self, left, right)

  def evaluate(self) -> int:
    return int(self.left.evaluate() / self.right.evaluate())


class MultiplyNode(Node, OperatorNode):
  def __init__(self, left: Optional[Node] = None, right: Optional[Node] = None):
    OperatorNode.__init__(self, left, right)
    
  def evaluate(self) -> int:
    return int(self.left.evaluate() * self.right.evaluate())


class SubtractNode(Node, OperatorNode):
  def __init__(self, left: Optional[Node] = None, right: Optional[Node] = None):
    OperatorNode.__init__(self, left, right)
    
  def evaluate(self) -> int:
    return int(self.left.evaluate() - self.right.evaluate())


class OperandNode(Node):
  def __init__(self, val: str):
    self.val = int(val)
    
  def evaluate(self) -> int:
    return int(self.val)


class OperandRegisty:
  def __init__(self):
    self._registry = {
      '+': AddNode,
      '-': SubtractNode,
      '/': DivideNode,
      '*': MultiplyNode,
    }

  def get(self) -> Dict:
    return self._registry


class TreeBuilder:
  
  def __init__(self, operand_registry: OperandRegisty = OperandRegisty()):
    self._operand_registry = operand_registry.get()

  def buildTree(self, postfix: List[str]) -> 'Node':
    stack = []
    for value in postfix:
      if value in self._operand_registry:
        operator = self.get_node(value)
        right = stack.pop()
        left = stack.pop()
        operator.left = left
        operator.right = right
        stack.append(operator)
      else:
        stack.append(self.get_node(value))
    return stack[0]
        
  def get_node(self, value: str) -> Node:
    if value in self._operand_registry:
      return self._operand_registry[value]()
    else:
      return OperandNode(value)
