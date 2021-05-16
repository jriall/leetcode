# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question
# to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:

# Input: haystack = "", needle = ""
# Output: 0


# Solution

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) == 0:
      return 0
    for i, haystack_char in enumerate(haystack):
      if i > len(haystack) - len(needle):
        return -1
      if haystack_char == needle[0]:
        match = True
        for j, needle_char in enumerate(needle):
          if needle_char != haystack[i + j]:
            match = False
            break
        if match == True:
          return i
    return -1