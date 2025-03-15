matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

filtered_matrix = [[num for num in row if num % 2 == 0] for row in matrix]

print(filtered_matrix)
