# import sys

# sys.stdin = open('input.txt', 'r')

# 220921 1245 균형점

# 정답코드

T = int(input())

def binary_search(start, end):
    mid = (start + end) / 2.0
    # print(mid, start, end)

    if start > end or abs(start - end) < 10**(-12):
        print('{:.10f}'.format(mid), end=' ')
        return mid

    power_left, power_right = power(mid)

    if power_left  == power_right:
        print('{:.10f}'.format(mid), end=' ')
        return mid

    elif power_left > power_right:
        binary_search(mid, end)
    else:
        binary_search(start, mid)


def power(mid):
    power_left = 0
    power_right = 0
    for i in range(N):
        if mid > loc[i]:
            power_left += weight[i] / (mid - loc[i])**2
        else:
            power_right += weight[i] / (mid - loc[i])**2
    
    return power_left, power_right


for t in range(1, T + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    
    loc = []
    weight = []
    for i in range(N):
        loc.append(temp[i])
        weight.append(temp[i + N])

    print('#{}'.format(t), end=' ')
    for i in range(N - 1):
        start = loc[i]
        end = loc[i + 1]
        binary_search(start, end)
    
    print()