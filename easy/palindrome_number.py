# Palindrome Number

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For
# example, 121 is palindrome while 123 is not.

# Example 1:

# Input: x = 121
# Output: true

import math

class Solution:
  def isPalindrome(self, x: int) -> bool:
    x_str = str(x)
    left = len(x_str) // 2 - 1
    right = math.ceil(len(x_str) / 2)
    while left >= 0 and right < len(x_str):
      if x_str[left] != x_str[right]:
        return False
      left -= 1
      right += 1
    return True