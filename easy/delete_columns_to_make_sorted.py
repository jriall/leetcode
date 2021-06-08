# Delete Columns to Make Sorted

# You are given an array of n strings strs, all of the same length.

# The strings can be arranged such that there is one on each line, making a
# grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically. In the
# above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e')
# are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column
# 1.

# Return the number of columns that you will delete.

# Example 1:

# Input: strs = ["cba","daf","ghi"]
# Output: 1
# Explanation: The grid looks as follows:
#   cba
#   daf
#   ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1
# column.

class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
    result = 0
    for col in range(len(strs[0])):
      is_sorted = True
      last_char_code = -1
      for row in range(len(strs)):
        char_code = ord(strs[row][col])
        if char_code < last_char_code:
          is_sorted = False
          break
        last_char_code = char_code
      if not is_sorted:
        result += 1
    return result
