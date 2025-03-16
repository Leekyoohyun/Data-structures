numList = [num*num for num in range(1, 6)]
print("%s" % numList)

numList = [num for num in range(1, 21) if num % 3 == 0]
print("%s" % numList)

#2차원 리스트
list2 = [[0 for _ in range(4)] for _ in range(3)]
print(list2)