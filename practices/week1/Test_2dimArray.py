list1 = []
list2 = []
value = 12

for i in range(0, 4):
    for j in range(0, 3):
        list1.append(value)
        value -= 1
    list2.append(list1)
    list1 = []

for i in range(0, 4):
    for j in range(0, 3):
        print("%3d" % list2[i][j], end = " ")
    print(" ")

