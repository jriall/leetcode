# Largest Odd Number in String

# You are given a string num, representing a large integer. Return the
# largest-valued odd integer (as a string) that is a non-empty substring of num,
# or an empty string "" if no odd integer exists.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the
# only odd number.

class Solution:
  def largestOddNumber(self, num: str) -> str:
    index = len(num) - 1
    while index >= 0:
      if int(num[index]) % 2 == 1:
        return num[:index + 1]
      index -= 1
    return ''
