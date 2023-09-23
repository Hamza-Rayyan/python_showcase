def min_matrix(n, m):
    # Get the dimensions of the input matrices
    rows = len(n)
    cols = len(n[0])

    # Initialize the result matrix with zeros
    result = [[0] * cols for _ in range(rows)]

    # Iterate through the matrices and compute the minimum
    for i in range(rows):
        for j in range(cols):
            result[i][j] = min(n[i][j], m[i][j])

    return result

# Example matrices
matrix_n = [[1, 2, 4], [4, 5, 0]]
matrix_m = [[1, 2, 0], [0, 0, 0]]

result_matrix = min_matrix(matrix_n, matrix_m)

# Print the result matrix
for row in result_matrix:
    print(row)
