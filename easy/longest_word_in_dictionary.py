# Longest Word in Dictionary

# Given an array of strings words representing an English Dictionary, return the
# longest word in words that can be built one character at a time by other words
# in words.

# If there is more than one possible answer, return the longest word with the
# smallest lexicographical order. If there is no answer, return the empty
# string.

# Example 1:

# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time b
# "w", "wo", "wor", and "worl".

class Solution:
  def longestWord(self, words: List[str]) -> str:
    words.sort()
    count = {}
    matches = ['']
    for word in words:
      count[word] = True
      is_match = True
      for i in range(len(word)):
        if word[0:i+1] not in count:
          is_match = False
          break
      if is_match:
        if len(word) == len(matches[0]):
          matches.append(word)
        elif len(word) > len(matches[0]):
          matches = [word]
    return matches[0]