# Lucky Numbers in a Matrix

# Given a m * n matrix of distinct numbers, return all lucky numbers in the
# matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element
# in its row and maximum in its column.

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row
# and the maximum in its column

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_row = []
        for row in matrix:
            min_in_row.append(min(row))
        max_in_col = []
        for col in range(len(matrix[0])):
            col_list = []
            for row in range(len(matrix)):
                col_list.append(matrix[row][col])
            max_in_col.append(max(col_list))
        result = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                num = matrix[row][col]
                if num == min_in_row[row] and num == max_in_col[col]:
                    result.append(num)
        return result
