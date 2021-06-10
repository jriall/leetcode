# Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution:
  def reverseWords(self, s: str) -> str:
    words = s.split(' ')
    for i, word in enumerate(words):
      reversed_word = []
      for j in reversed(range(len(word))):
        reversed_word.append(word[j])
      words[i] = ''.join(reversed_word)
    return ' '.join(words)
