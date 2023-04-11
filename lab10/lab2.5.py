def matrix_operation(matrix1, matrix2, operation):
    
    n1, m1 = len(matrix1), len(matrix1[0])
    n2, m2 = len(matrix2), len(matrix2[0])
    
    if operation in ['+', '-'] and (n1 != n2 or m1 != m2):
        raise ValueError("Размерности матриц не совпадают")

    if operation == '+':
        result = [[matrix1[i][j] + matrix2[i][j] for j in range(m1)] for i in range(n1)]
    elif operation == '-':
        result = [[matrix1[i][j] - matrix2[i][j] for j in range(m1)] for i in range(n1)]
    elif operation == '*':
        if m1 != n2:
            raise ValueError("Несовместимые размерности матриц")
        result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(m1)) for j in range(m2)] for i in range(n1)]
    else:
        raise ValueError("Некорректная операция")

    return result


A = []
B = []
while True:
    row = input("Введите строку матрицы A: ")
    if not row:
        break
    row = list(map(int, row.split(",")))
    A.append(row)

while True:
    row = input("Введите строку матрицы B: ")
    if not row:
        break
    row = list(map(int, row.split(",")))
    B.append(row)

operation = input("Введите операцию: ")

C = matrix_operation(list(zip(*A)), list(zip(*B)), operation)
C = [list(row) for row in zip(*C)] 

for i, row in enumerate(C):
    for j, value in enumerate(row):
        print(f"C[{i}][{j}] = {value}")
for row in C:
    print(row)
