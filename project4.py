R = int(input("Enter the Number of rows : "))
C = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix:")
matrixA = [[int(input()) for i in range(C)] for i in range(R)]
print("First Matrix is: ")
for n in matrixA:
    print(n)

print("Enter the elements of Second Matrix:")
matrixB = [[int(input()) for i in range(C)] for i in range(R)]
for n in matrixB:
    print(n)

result = [[0 for i in range(C)] for i in range(R)]

for i in range(R):
    for j in range(C):
        result[i][j] = matrixA[i][j] + matrixB[i][j]

print("The Sum is : ")
for r in result:
    print(r)

for i in range(R):
    for j in range(C):
        result[i][j] = matrixA[i][j] - matrixB[i][j]
print("The Diff is:")
for r in result:
    print(r)

for i in range(R):
    for j in range(C):
        result[i][j] = matrixA[i][j] * matrixB[i][j]
print("The multiplication is: ")
for r in result:
    print(r)


