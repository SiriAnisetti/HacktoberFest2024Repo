rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix_a = []
matrix_b = []
result = []

print("Enter matrix A:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix_a.append(row)

print("Enter matrix B:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix_b.append(row)

for i in range(rows):
    result_row = []
    for j in range(cols):
        result_row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(result_row)

print("Resultant Matrix:")
for row in result:
    print(" ".join(map(str, row)))
