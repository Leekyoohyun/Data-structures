# 문제 1
list = [num for num in range(1,101) if num % 5 == 0 or num % 3 == 0]
print(list)

# 문제 2
matrix = [[1,2,3], [4,5,6], [7,8,9]]

matrix2 = [[num for num in row if num % 2 == 0] for row in matrix]
print(matrix2)

# 문제 3
original_tuple = (1,2,3)
new_tuple = original_tuple+(4,)
print(new_tuple)

# 문제 4
import random
lotto_list = []
lotto_number_count = (int)(input("Enter number of sets : "))

lotto_list = [random.sample(range(1, 46), 6) for _ in range(lotto_number_count)]

lotto_list.sort()
for numbers in lotto_list:
    print(numbers)