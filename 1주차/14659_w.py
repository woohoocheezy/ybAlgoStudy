from sys import stdin

n = int(stdin.readline())
dragons = list(map(int, stdin.readline().split()))
points = [0] * n

while True:

    for i in range(len(dragons) - 1):

        if dragons[i] > dragons[i + 1]:
            points[i] += 1
            dragons[i + 1] = 0

    for i, a_dragon in enumerate(dragons):
        if a_dragon == 0:
            points.pop(i)
            dragons.remove(a_dragon)

    print(dragons)
    print(points)
    print()

    if len(dragons) == 0 or dragons == sorted(dragons):
        break

print(max(points))
