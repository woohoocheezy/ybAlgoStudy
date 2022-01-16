from sys import stdin

n = int(stdin.readline())
s = list(map(int, stdin.readline().split()))

s.sort()

min = 200000
for i in range(n):
    sum = s[i] + s[2 * n - i - 1]

    if sum < min:
        min = sum

print(min)
