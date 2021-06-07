# Flipping an Image

# Given an n x n binary matrix image, flip the image horizontally, then invert
# it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.

# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced
# by 0.

# For example, inverting [0,1,1] results in [1,0,0].

# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

class Solution:
  def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    for row in image:
      start = 0
      end = len(row) - 1
      while start < end:
        row[start] = 1 - row[start]
        row[end] = 1 - row[end]
        row[start], row[end] = row[end], row[start]
        start += 1
        end -= 1
      if len(row) % 2 == 1:
        middle = len(row) // 2
        row[middle] = 1 - row[middle]
    return image
