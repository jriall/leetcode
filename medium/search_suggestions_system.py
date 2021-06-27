# Search Suggestions System

# Given an array of strings products and a string searchWord. We want to design
# a system that suggests at most three product names from products after each
# character of searchWord is typed. Suggested products should have common prefix
# with the searchWord. If there are more than three products with a common
# prefix return the three lexicographically minimums products.

# Return list of lists of the suggested products after each character of
# searchWord is typed. 

 

# Example 1:

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    trie = Trie()
    for word in products:
      trie.insert(word)
    return trie.get_search_results(searchWord, products)
    
    
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
  
  def get_search_results(self, searchTerm, products):
    results = []
    curr = self.trie
    products.sort()
    letters = []
    for letter in searchTerm:
      letters.append(letter)
      if letter in curr:
        matches = [word for word in products if word.startswith(''.join(letters))]
        results.append(matches[:3])
        curr = curr[letter]
      else:
        results.append([])
        curr = {}
    return results
        