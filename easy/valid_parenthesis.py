# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true

class Solution:
  def isValid(self, s: str) -> bool:
    queue = []
    brackets = {
      ']': '[',
      ')': '(',
      '}': '{',
    }
    for char in s:
      if char in brackets.values():
        queue.append(char)
      else:
        if len(queue) == 0:
          return False
        end = queue.pop()
        if brackets[char] != end:
          return False
    return len(queue) == 0
