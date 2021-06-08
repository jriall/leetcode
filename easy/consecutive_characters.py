# Consecutive Characters

# Given a string s, the power of the string is the maximum length of a
# non-empty substring that contains only one unique character.

# Return the power of the string.

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.

class Solution:
  def maxPower(self, s: str) -> int:
    max_len = 0
    current_count = 0
    current_char = ''
    for char in s:
      if current_char == char:
        current_count += 1
      else:
        current_char = char
        current_count = 1
      max_len = max(max_len, current_count)
    return max_len