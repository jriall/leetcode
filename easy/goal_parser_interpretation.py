# Goal Parser Interpretation

# You own a Goal Parser that can interpret a string command. The command
# consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal
# Parser will interpret "G" as the string "G", "()" as the string "o", and
# "(al)" as the string "al". The interpreted strings are then concatenated in
# the original order.

# Given the string command, return the Goal Parser's interpretation of command.

# Example 1:

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

class Solution:
  def interpret(self, command: str) -> str:
    index = 0
    result = []
    while index < len(command):
      if command[index] == 'G':
        result.append('G')
        index += 1
      elif command[index + 1] == ')':
        result.append('o')
        index += 2
      else:
        result.append('al')
        index += 4
    return ''.join(result)

class Solution:
  def interpret(self, command: str) -> str:
    mapping = {
      'G': 'G',
      '()': 'o',
      '(al)': 'al',
    }
    result = []
    temp = ''
    for char in command:
      temp += char
      if temp in mapping:
        result.append(mapping[temp])
        temp = ''
    return ''.join(result)
