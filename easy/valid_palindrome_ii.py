# Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

class Solution:
  def validPalindrome(self, s: str, can_delete = True) -> bool:
    start = 0
    end = len(s) - 1
    while start <= end:
      if s[start] == s[end]:
        start += 1
        end -= 1
      elif can_delete:
        start_removed = self.validPalindrome(s[start + 1:end + 1], False)
        end_removed = self.validPalindrome(s[start:end], False)
        return start_removed or end_removed
      else:
        return False
    return True