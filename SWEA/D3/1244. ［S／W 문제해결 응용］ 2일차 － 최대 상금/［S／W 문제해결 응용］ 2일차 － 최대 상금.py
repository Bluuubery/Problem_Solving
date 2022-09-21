# import sys

# sys.stdin = open('input.txt', 'r')

# 220921 swea 1244

# 정답코드

T = int(input())


def prize(number):
    prize = 0
    for i in range(len(number)):
        prize += number[i] * 10**(len(number) - i - 1)
    return prize


def back_tracking(current, depth):
    global ans

    if depth == change:
        ans = max(ans, prize(number))

        return

    if number == sorted(number, reverse=True):
        if (change - depth) % 2:
            number[-1], number[-2] = number[-2], number[-1]
            back_tracking(0, change)
            number[-1], number[-2] = number[-2], number[-1]
        else:
            ans = prize(number)
            return
    
    
    for i in range(current, len(number)):
        for j in range(i + 1, len(number)):
            if number[i] <= number[j]:

                number[i], number[j] = number[j], number[i]

                back_tracking(i, depth + 1)

                number[i], number[j] = number[j], number[i]

    



for t in range(1, T + 1):
    number, change = input().split()
    number = list(map(int, number))
    change = int(change)

    ans = 0

    back_tracking(0, 0)


    print('#{} {}'.format(t, ans))

    