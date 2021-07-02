# Replace Words

# In English, we have a concept called root, which can be followed by some other
# word to form another longer word - let's call this word successor. For
# example, when the root "an" is followed by the successor word "other", we can
# form a new word "another".

# Given a dictionary consisting of many roots and a sentence consisting of words
# separated by spaces, replace all the successors in the sentence with the root
# forming it. If a successor can be replaced by more than one root, replace it
# with the root that has the shortest length.

# Return the sentence after the replacement.

# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

class Solution:
  def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    trie = Trie()
    for word in dictionary:
      trie.insert(word)
    result = sentence.split(' ')
    for index in range(len(result)):
      result[index] = trie.search_for_root(result[index])
    return ' '.join(result)


class Trie:
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
  
  def search_for_root(self, word):
    curr = self.trie
    for index in range(len(word)):
      if self.endSymbol in curr:
        return word[:index]
      elif word[index] not in curr:
        return word
      else:
        curr = curr[word[index]]
    return word
    