# Implement Magic Dictionary

# Design a data structure that is initialized with a list of different words.
# Provided a string, you should determine if you can change exactly one
# character in this string to match any word in the data structure.

# Implement the MagicDictionary class:

# MagicDictionary() Initializes the object.
# void buildDict(String[] dictionary) Sets the data structure with an array of
# distinct strings dictionary.
# bool search(String searchWord) Returns true if you can change exactly one
# character in searchWord to match any string in the data structure, otherwise
# returns false.
 

# Example 1:

# Input
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
# [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
# Output
# [null, null, false, true, false, false]

# Explanation
# MagicDictionary magicDictionary = new MagicDictionary();
# magicDictionary.buildDict(["hello", "leetcode"]);
# magicDictionary.search("hello"); // return False
# magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to
# match "hello" so we return True
# magicDictionary.search("hell"); // return False
# magicDictionary.search("leetcoded"); // return False

class MagicDictionary:
  
  def __init__(self):
    self.dictionary = {}  

  def buildDict(self, dictionary: List[str]) -> None:
    for word in dictionary:
      self.dictionary[word] = [ord(letter) for letter in word]
      
  def search(self, searchWord: str) -> bool:
    for letter_values in self.dictionary.values():
      if len(letter_values) != len(searchWord):
        continue
      else:
        letters_different = 0
        for index, letter_value in enumerate(letter_values):
          print(letter_value, ord(searchWord[index]))
          if letter_value != ord(searchWord[index]):
            letters_different += 1
        if letters_different == 1:
          return True
    return False
            