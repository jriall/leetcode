# Longer Contiguous Segments of Ones than Zeros

# Given a binary string s, return true if the longest contiguous segment of 1s
# is strictly longer than the longest contiguous segment of 0s in s. Return
# false otherwise.

# For example, in s = "110100010" the longest contiguous segment of 1s has
# length 2, and the longest contiguous segment of 0s has length 3.
# Note that if there are no 0s, then the longest contiguous segment of 0s is
# considered to have length 0. The same applies if there are no 1s.

# Example 1:

# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.

class Solution:
  def checkZeroOnes(self, s: str) -> bool:
    if len(s) == 1:
      return s == '1'
    max_zeroes = 0
    max_ones = 0
    current_count = {
      'num': s[0],
      'count': 1,
    }
    for index in range(1, len(s)):
      if s[index] == current_count['num']:
        current_count['count'] += 1
      else:
        if current_count['num'] == '0':
          max_zeroes = max(current_count['count'], max_zeroes)
        else:
          max_ones = max(current_count['count'], max_ones)
        current_count['num'] = s[index]
        current_count['count'] = 1
    if current_count['num'] == '0':
      max_zeroes = max(current_count['count'], max_zeroes)
    else:
      max_ones = max(current_count['count'], max_ones)
    print(max_ones, max_zeroes)
    return max_ones > max_zeroes


# Simplified solution

class Solution:
  def checkZeroOnes(self, s: str) -> bool:
    count_zero = 0
    count_one = 0
    max_zero = 0
    max_one = 0
    for char in s:
      if char == '1':
        count_one += 1
        count_zero = 0
      else:
        count_zero += 1
        count_one = 0
      max_zero = max(max_zero, count_zero)
      max_one = max(max_one, count_one)
    return count_one > count_zero