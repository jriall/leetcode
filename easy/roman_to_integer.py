# Roman to integer

VALUES = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}

PREFIXED_VALUES = {
  'IV': 4,
  'IX': 9, 
  'XL': 40,
  'XC': 90,
  'CD': 400,
  'CM': 900,
}

class Solution:
  def romanToInt(self, s: str) -> int:
    total = 0
    index = len(s) - 1
    while index >= 0:
      print(index, s[index])
      if index > 0 and s[index-1:index+1] in PREFIXED_VALUES:
        total += PREFIXED_VALUES[s[index-1:index+1]]
        index -= 2
      elif s[index] in VALUES:
        total += VALUES[s[index]]
        index -= 1
    return total