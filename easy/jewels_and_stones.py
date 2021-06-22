# Jewels and Stones

# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a
# type of stone you have. You want to know how many of the stones you have are
# also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone
# from "A".

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

class Solution:
  def numJewelsInStones(self, jewels: str, stones: str) -> int:
    jewel_definitions = {}
    for jewel in jewels:
      jewel_definitions[jewel] = True
    result = 0
    for stone in stones:
      if stone in jewel_definitions:
        result += 1
    return result
