# Camelcase Matching

# A query word matches a given pattern if we can insert lowercase letters to the
# pattern word so that it equals the query. (We may insert each character at any
# position, and may insert 0 characters.)

# Given a list of queries, and a pattern, return an answer list of booleans,
# where answer[i] is true if and only if queries[i] matches the pattern.

# Example 1:
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation: 
# "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

# Example 2:
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
# Output: [true,false,true,false,false]
# Explanation: 
# "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".

class Solution:
  def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    trie = Trie()
    trie.insert(pattern)
    return [trie.match(word) for word in queries]


class Trie():
  def __init__(self):
    self.trie = {}
    self.endSymbol = '*'

  def insert(self, word):
    curr = self.trie
    for letter in word:
      if letter not in curr:
        curr[letter] = {}
      curr = curr[letter]
    curr[self.endSymbol] = True

  def match(self, word):
    curr = self.trie
    for letter in word:
      if letter == letter.upper():
        if letter in curr:
          curr = curr[letter]
        else:
          return False
      else:
        if letter in curr:
          curr = curr[letter]
        else:
          continue
    return self.endSymbol in curr
