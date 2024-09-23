
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


transposed_matrix = transpose_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
