# Reverse Only Letters

# Given a string s, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their positions.

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"

class Solution:
  def reverseOnlyLetters(self, s: str) -> str:
    start = 0
    end = len(s) - 1
    result = [char for char in s]
    while start < end:
      if result[start].isalpha() and result[end].isalpha():
        result[start], result[end] = result[end], result[start]
        start += 1
        end -= 1
      elif result[start].isalpha():
        end -= 1
      elif result[end].isalpha():
        start += 1
      else:
        start += 1
        end -= 1
    return ''.join(result)