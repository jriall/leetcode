# Partition Labels

# You are given a string s. We want to partition the string into as many parts
# as possible so that each letter appears in at most one part.

# Return a list of integers representing the size of these parts.

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits s into less parts.

class Solution(object):
  def partitionLabels(self, s: str):
    hashtable = {}
    results = []
    count = 0
    for i in range(len(s)):
      hashtable[s[i]] = i
    i = 0
    while(i < len(s)):
      j = hashtable[s[i]]
      while(i < j):
        if hashtable[s[i]] > j:
          j = hashtable[s[i]]
        count += 1
        i += 1
      i += 1
      count += 1
      results.append(count)
      count = 0
    return results
