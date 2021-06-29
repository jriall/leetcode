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

class Solution:
  def romanToInt(self, s: str) -> int:
    total = VALUES[s[-1]]
    index = len(s) - 2
    while index >= 0:
      value = VALUES[s[index]]
      previous_value = VALUES[s[index + 1]]
      total += value if value >= previous_value else -value
      index -= 1
    return total
