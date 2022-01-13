row = abs(int(input('Please enter the row num : ')))
matrix = [[1 for i in range(row)] for j in range(row)]
for i in range(row):
    for j in range(1, i):
        matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
for i in range(row):
    for j in range(i + 1):
        print(matrix[i][j], end=' ')
    print('\n')