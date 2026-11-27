r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
A = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

print("Enter elements of second matrix:")
B = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    B.append(row)

# Addition of two matrices
C = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Addition of two matrices:")
for row in C:
    print(row)  

Enter number of rows: 2
Enter number of columns: 2

Using Python List

Enter elements of first matrix:
1
2
3
4

Enter elements of second matrix:
5
6
7
8

Addition of two matrices:
[6, 8]
[10, 12]

Using Numpy Array

import numpy as np

# Accept matrix elements
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
A = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

print("Enter elements of second matrix:")
B = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    B.append(row)

# Convert lists into NumPy arrays
A = np.array(A)
B = np.array(B)

# Addition of matrices
C = A + B

print("Addition of two matrices:")
print(C)

Enter number of rows: 2
Enter number of columns: 2

Enter elements of first matrix:
1
2
3
4

Enter elements of second matrix:
5
6
7
8

Addition of two matrices:
[[ 6  8]
 [10 12]]
