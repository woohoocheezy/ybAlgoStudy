from sys import stdin

n, m = map(int, stdin.readline().split())
cakes = list(map(int, stdin.readline().split()))

cakes.sort()

count = m
available_cakes = 0

for a_cake in cakes:
    if a_cake == 10:
        available_cakes += 1
        continue

    if a_cake % 10 == 0:
        a_cake_pieces = a_cake // 10
        if a_cake_pieces < count:
            count -= a_cake_pieces
            available_cakes += a_cake_pieces
        elif a_cake_pieces == count:
            print(available_cakes)
            break
        else:
            available_cakes += count
            print(available_cakes)
            break
    print(f"count : {count} available_cakes : {available_cakes}")
