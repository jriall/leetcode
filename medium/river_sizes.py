# River Sizes

# You're given a two-dimensional array (a matrix) of potentially unequal height
# and width containing only 0s and 1s. Each 0 represents land, and each 1
# represents part of a river. A river consists of any number of 1s that are
# either horizontally or vertically adjacent (but not diagonally adjacent). The
# number of adjacent 1s forming a river determine its size.

# Note that a river can twist. In other words, it doesn't have to be a straight
# vertical line or a straight horizontal line; it can be L-shaped, for example.

# Write a function that returns an array of the sizes of all rivers represented
# in the input matrix. The sizes don't need to be in any particular order.

# Sample Input
# matrix = [
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0],
# ]
# Sample Output
# [1, 2, 2, 2, 5] // The numbers could be ordered differently.

# // The rivers can be clearly seen here:
# // [
# //   [1,  ,  , 1,  ],
# //   [1,  , 1,  ,  ],
# //   [ ,  , 1,  , 1],
# //   [1,  , 1,  , 1],
# //   [1,  , 1, 1,  ],
# // ]

from collections import deque

def riverSizes(matrix):
  result = []
  seen_matrix = [[False for n in range(len(matrix[0]))] for n in range(len(matrix))]
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 1 and seen_matrix[i][j] == False:
        traverse_nodes(matrix, i, j, seen_matrix, result)
  return result

def traverse_nodes(matrix, i, j, seen_matrix, result):
  river_size = 0
  stack = deque([[i, j]])
  while len(stack):
    next_i, next_j = stack.popleft()
    if matrix[next_i][next_j] == 0 or seen_matrix[next_i][next_j] == True:
      continue
    if seen_matrix[next_i][next_j] == False:
      river_size += 1
      seen_matrix[next_i][next_j] = True
      if next_i - 1 >= 0:
        stack.append([next_i - 1, next_j])
      if next_j + 1 < len(matrix[0]):
        stack.append([next_i, next_j + 1])
      if next_i + 1 < len(matrix):
        stack.append([next_i + 1, next_j])
      if next_j - 1 >= 0:
        stack.append([next_i, next_j - 1])
  if river_size != 0:
    result.append(river_size)