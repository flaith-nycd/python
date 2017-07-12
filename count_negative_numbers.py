# Python implementation of Efficient method to count of
# negative numbers in M[n][m]


def count_negative(matrix, totalrow, totalcol):
    count = 0  # initialize result

    # Start with top right corner
    current_row = 0
    current_col = totalcol - 1

    # Follow the path shown using arrows above
    while current_col >= 0 and current_row < totalrow:

        if matrix[current_row][current_col] < 0:

            # j is the index of the last negative number
            # in this row. So there must be ( currentCol+1 )
            count += (current_col + 1)

            # negative numbers in this row.
            current_row += 1

        else:
            # move to the left and see if we can
            # find a negative number there
            current_col -= 1
    return count


# Driver code
Matrix = [
    [-3, -2, -1, 1],
    [-2, 2, 3, 4],
    [4, 5, 7, 8]
]
print(count_negative(Matrix, 3, 4))

# Driver code
Matrix = [
    [-11, -10, -9, -8, -7],
    [-6, -5, -4, -3, -2],
    [-1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]
print(count_negative(Matrix, 4, 5))
