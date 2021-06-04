# Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

# Example 1:

# Input: s = "hello"
# Output: "holle"

class Solution:
  def reverseVowels(self, s: str) -> str:
    arr = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u']
    start = 0
    end = len(s) - 1
    while start < end:
      if arr[start].lower() in vowels and arr[end].lower() in vowels:
        arr[start], arr[end] = arr[end], arr[start]
        end -= 1
        start += 1
      elif arr[start].lower() in vowels:
        end -= 1
      else:
        start += 1
    return ''.join(arr)
        