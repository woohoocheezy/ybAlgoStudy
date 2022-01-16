from sys import stdin

n = int(stdin.readline())
dragons = list(map(int, stdin.readline().split()))
# points = [0] * n

best_score = -1

for i in range(len(dragons) - 1):
    i_point = 0
    for j in range(i + 1, len(dragons)):
        if dragons[i] > dragons[j]:
            i_point += 1
        else:
            break

    if i_point > best_score:
        best_score = i_point

print(best_score)
