# Bulb Switcher III

# There is a room with n bulbs, numbered from 1 to n, arranged in a row from
# left to right. Initially, all the bulbs are turned off.

# At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb
# change color to blue only if it is on and all the previous bulbs (to the left)
# are turned on too.

# Return the number of moments in which all turned on bulbs are blue.

# Example 1:

# Input: light = [2,1,3,5,4]
# Output: 3
# Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.

class Solution:
  def numTimesAllBlue(self, lights: List[int]) -> int:
    occurances = 0
    high = 0
    bulb = 0
    for light in lights:
      high = max(high, light)
      bulb += 1
      if high == bulb:
        occurances += 1
      
    return occurances