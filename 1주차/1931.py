from sys import stdin

n = int(stdin.readline())
meeting_info = []

for _ in range(n):
    meeting_info.append(list(map(int, stdin.readline().split())))

meeting_info.sort(key=lambda x: (x[1], x[0]))

current_end_time = 0
cnt = 0

for a_meeting in meeting_info:
    if current_end_time <= a_meeting[0]:
        cnt += 1
        current_end_time = a_meeting[1]


print(cnt)
