from sys import stdin

n = int(stdin.readline())
levels = []
for _ in range(n):
    levels.append(int(stdin.readline()))

cnt = 0

for i in range(n - 1, 0, -1):
    if levels[i] <= levels[i - 1]:
        cnt += levels[i - 1] - levels[i] + 1
        levels[i - 1] -= levels[i - 1] - levels[i] + 1

print(cnt)
