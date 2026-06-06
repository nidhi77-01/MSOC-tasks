n = int(input("Enter size of square matrix: "))

matrix = []

print("Enter matrix elements:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary = 0
secondary = 0

for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[i][n - 1 - i]

print("Primary Diagonal Sum =", primary)
print("Secondary Diagonal Sum =", secondary)
