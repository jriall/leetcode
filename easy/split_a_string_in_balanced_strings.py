# Split a String in Balanced Strings

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount of balanced strings.

# Return the maximum amount of split balanced strings.

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

class Solution:
  def balancedStringSplit(self, s: str) -> int:
    char_count = 0
    result = 0
    for char in s:
      if char == 'L':
        char_count += 1
      else:
        char_count -= 1
      if char_count == 0:
        result += 1
    return result