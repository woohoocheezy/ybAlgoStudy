from sys import stdin

n = int(stdin.readline())

minM = n + 1
isHave = 0

for i in range(1, n):
    temp = i
    tempSum = i

    while temp // 10 != 0:
        tempSum += temp % 10
        temp = temp // 10

    tempSum += temp

    if tempSum == n:
        isHave = 1
        minM = i
        break

if isHave == 0:
    print(0)
else:
    print(minM)
