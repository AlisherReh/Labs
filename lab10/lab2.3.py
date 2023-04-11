def rotate_matrix_clockwise(matrix):
    
    return [list(reversed(row)) for row in zip(*matrix)]

print()

matrix = []

while True:
    row = input("Введите строку матрицы: ")
    if not row:
        break
    row = list(map(int, row.split(",")))
    matrix.append(row)

for row in matrix:
    print(row)
print()

rotated = rotate_matrix_clockwise(matrix)
for row in rotated:
    print(row)