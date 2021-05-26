# Reverse string

# Write a function that reverses a string. The input string is given as an
# array of characters s.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.

class Solution:
  def reverseString(self, s: List[str]) -> None:
    for i in range(len(s) // 2):
      j = len(s) - i - 1
      s[i], s[j] = s[j], s[i]