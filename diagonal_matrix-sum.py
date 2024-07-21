import random
def sum_of_diagonalsmatrix():
    sum_primary = 0
    sum_secondary = 0
    for i in range(len(matrix)):
        sum_primary += matrix[i][i]
        sum_secondary += matrix[i][len(matrix) - i - 1]
    return sum_primary, sum_secondary


def create_matrix():
    matrix = []
    for i in range(3):
        row = []
        for j in range(4):
            row.append(random.randint(1, 10))
        matrix.append(row)
    return matrix

matrix = create_matrix()
print("Matrix:")
for row in matrix:
    print(row)

# Calculate sum of diagonal elements
sum_primary, sum_secondary = sum_of_diagonalsmatrix()

print("\nSum of primary diagonal elements: ", sum_primary)
print("Sum of secondary diagonal elements: ", sum_secondary)