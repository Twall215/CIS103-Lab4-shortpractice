#Creating the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Now looping through
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(f"Row: {row}, Column {col}: {matrix[row][col]}")