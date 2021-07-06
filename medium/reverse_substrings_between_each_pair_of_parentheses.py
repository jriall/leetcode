# Reverse Substrings Between Each Pair of Parentheses

# You are given a string s that consists of lower case English letters and
# brackets. 

# Reverse the strings in each pair of matching parentheses, starting from the
# innermost one.

# Your result should not contain any brackets.

# Example 1:

# Input: s = "(abcd)"
# Output: "dcba"

class Solution:
  def reverseParentheses(self, s: str) -> str:
    stack = []
    bracket_pairs = []
    for index in range(len(s)):
      if s[index] == '(':
        stack.append(index)
      elif s[index] == ')':
        next = stack.pop()
        bracket_pairs.append([next, index])
    result = [char for char in s]
    for pair in bracket_pairs:
      start = pair[0]
      end = pair[1]
      while start < end:
        result[start], result[end] = result[end], result[start]
        start += 1
        end -= 1
    return ''.join([char for char in result if char not in ['(', ')']])