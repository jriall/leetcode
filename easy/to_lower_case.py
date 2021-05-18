# To Lower Case

# Implement function ToLowerCase() that has a string parameter str, and returns
# the same string in lowercase.

class Solution:
  def toLowerCase(self, str: str) -> str:
    result = []
    for char in str:
      ascii_value = ord(char)
      if 65 <= ascii_value <= 90:
        result.append(chr(ascii_value + 32))
      else:
        result.append(char)
    return ''.join(result)