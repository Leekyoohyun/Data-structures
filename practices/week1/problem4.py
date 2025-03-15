import random

num_sets = int(input("Enter number of sets: "))

lotto_numbers = [sorted(random.sample(range(1, 46), 6)) for _ in range(num_sets)]

for numbers in lotto_numbers:
    print(numbers)
