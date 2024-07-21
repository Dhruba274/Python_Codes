
rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))
rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))

if cols1 != rows2:
    print("Error: The number of columns in matrix 1 must match the number of rows in matrix 2.")
    exit()

matrix1 = []
matrix2 = []

print("Enter the elements of matrix 1:")

for i in range(rows1):
    row = []
    for j in range(cols1):
        element = int(input("Enter element at position row wisely "))
        row.append(element)
    matrix1.append(row)

print("Enter the elements of matrix 2:")

for i in range(rows2):
    row = []
    for j in range(cols2):
        element = int(input("Enter element rowwisely "))
        row.append(element)
    matrix2.append(row)


result = [[0] * cols2 for _ in range(rows1)]

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Result Matrix:")
for row in result:
    print(row)