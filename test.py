matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows = len(matrix)
cols = len(matrix)

for col in range(cols):
    for row in range(rows):
        print(matrix[row][col], end=" ")
    print()
