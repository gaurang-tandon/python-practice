# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.

def matrix_construct(x, y):
    matrix = []
    rows = []
    for i in range(x):
        coloumn = []
        for j in range(y):
            coloumn.append(i*j)
        rows.append(coloumn)
    matrix.append(rows)
    return matrix


matrix_1 = matrix_construct(3, 5)
for k in matrix_1:
    print(k)
