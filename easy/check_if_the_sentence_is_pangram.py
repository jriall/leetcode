# Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at
# least once.

# Given a string sentence containing only lowercase English letters, return true
# if sentence is a pangram, or false otherwise.

 
# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English
# alphabet.

class Solution:
  def checkIfPangram(self, sentence: str) -> bool:
    if len(sentence) < 26:
      return False
    letters_used = 0
    letter_cache = {}
    for char in sentence:
      if char not in letter_cache:
        letter_cache[char] = True
        letters_used += 1
    return letters_used >= 26