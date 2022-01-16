from sys import stdin

n, m = map(int, stdin.readline().split())
cakes = list(map(int, stdin.readline().split()))

cakes.sort()

count = m
available_cakes = 0

for a_cakes in cakes :
    if a_cakes == 10 :
        available_cakes += 1

    elif a_cakes % 10 == 0 :
        if (a_cakes // 10 ) - 1 == count :
            # print("#", count)
            available_cakes += count + 1
            count 
            # print(available_cakes)
            # break

        elif (a_cakes // 10 ) - 1 < count :
            # print("@", count)
        # else :
            available_cakes += a_cakes // 10
            count -= a_cakes // 10 - 1

        else : # a_cakes // 10 > count 
            # print("^", count)
            available_cakes += count
            count 
            # print(available_cakes)
            # break

    else :
        if a_cakes // 10 == count :
            # print("%", count)
            available_cakes += count
            # print(available_cakes)
            # break
        elif a_cakes // 10 < count :
            # print("$", count)
            available_cakes += a_cakes // 10
            count -= a_cakes // 10 
        else:
            # print("*", count)
            available_cakes += count
            print(available_cakes)
            break
else:
    print(available_cakes)
