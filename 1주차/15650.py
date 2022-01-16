from sys import stdin


def find_result(a_list):

    if len(a_list) == m:
        for i in a_list:
            print(i, end=" ")
        print()

    else:
        for i in given_list:
            if len(a_list) == 0 or (i not in a_list and a_list[-1] < i):
                a_list.append(i)
                find_result(a_list)
                a_list.pop()


n, m = map(int, stdin.readline().split())
given_list = list(range(1, n + 1))

find_result([])
