# Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding
# letters in alternating order, starting with word1. If a string is longer than
# the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    result = []
    index_one = 0
    index_two = 0
    while index_one < len(word1) or index_two < len(word2):
      if index_one < len(word1):
        result.append(word1[index_one])
        index_one += 1
      if index_two < len(word2):
        result.append(word2[index_two])
        index_two += 1
    return ''.join(result)