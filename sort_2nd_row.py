import numpy as np

# Create a random matrix
matrix = np.random.randint(0, 100, size=(4, 4))

# Sort the matrix with respect to the second row
sorted_matrix = matrix[np.argsort(matrix[:, 1])]

print("Original matrix:")
print(matrix)

print("\nSorted matrix:")
print(sorted_matrix)