# Count the Number of Consistent Strings

# You are given a string allowed consisting of distinct characters and an array
# of strings words. A string is consistent if all characters in the string
# appear in the string allowed.

# Return the number of consistent strings in the array words.

# Example 1:

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain
# characters 'a' and 'b'.

class Solution:
  def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    allowed_hashtable = {}
    for char in allowed:
      allowed_hashtable[char] = True
    results = 0
    for word in words:
      is_consistent = True
      for char in word:
        if char not in allowed_hashtable:
          is_consistent = False
          break
      if is_consistent:
        results += 1
    return results