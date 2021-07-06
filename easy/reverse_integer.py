# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).

# Example 1:

# Input: x = 123
# Output: 321

import math

class Solution:
  def reverse(self, x: int) -> int:
    if x == 0:
      return 0
    val = abs(x)
    multiplier = 1 if abs(x) == x else - 1
    nums = []
    while val > 0:
      digit = val % 10
      nums.append(str(digit))
      val = val // 10
    result = int(''.join(nums)) * multiplier
    return 0 if abs(result) > math.pow(2, 31) else result
