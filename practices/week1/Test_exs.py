numList = []
for num in range(1, 101):
    if num % 2 == 0:
        numList.append(num)

print(numList)

# aa = []
#
# for i in range(0,4):
#     aa.append(0)
# sum = 0
#
# for i in range(0, 4):
#     aa[i] = int(input(str(i+1)+"번째 숫자 : "))
#
# for i in range(0, 4):
#     sum += aa[i]
#
# print("sum = %d" % sum)

bb = [10, 20, 30, 40]
print(bb[-4])

myList = [30, 10, 20]
print("현재 리스트: %s" % myList)

myList.append(40)
print("append 후의 리스트: %s" % myList)

print("pop()으로 추출한 값 : %s" % myList.pop())
print("pop 이후 리스트 : %s" % myList)

myList.sort()
print("sort 후 리스트 : %s" % myList)

myList.reverse()
print("reverse 후 리스트 : %s" % myList)

print("값 20의 위치 : %d" % myList.index(20))

myList.insert(2, 222)
print("insert한 후 리스트 : %s" % myList)

myList.remove(222)
print("remove 후 리스트 : %s" % myList)

myList.extend([77, 88, 77])
print("extend 후 리스트 : %s" % myList)

print("77 값의 개수 : %d" % myList.count(77))

list1 = []
list2 = []
value = 1

for i in range(0, 3):
    for j in range(0, 4):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []

for i in range(0, 3):
    for j in range(0, 4):
        print("%3d" % list2[i][j], end = " ")
    print(" ")


ss = 'python을 열심히 공부 중'
listSplit = ss.split()
print(listSplit)

ss = '하나:둘:셋'
listSplit = ss.split(':')
print(listSplit)

ss = '하나\n둘\n셋'
listSplit = ss.splitlines()
print(listSplit)

ss = '%'
listSplit = ss.join('파이썬')
print(listSplit)

before = ['2022', '12', '31']
after = list(map(int, before))
print(after)
print(type(after[0])) # int형으로 변환

tt1 = (10, 20, 30); tt1
tt2 = 10, 20, 30; tt2 # 소괄호 생략 가능

print(tt1)
print(tt2)