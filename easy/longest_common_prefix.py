# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of
# strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    shortest = float('inf')
    for word in strs:
      shortest = min(shortest, len(word))
    result = []
    for i in range(shortest):
      letter = strs[0][i]
      for j in range(1, len(strs)):
        if letter != strs[j][i]:
          return ''.join(result)
      result.append(letter)
    return ''.join(result)