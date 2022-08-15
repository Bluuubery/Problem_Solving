T = int(input())

for t in range(1, T + 1):
    N = int(input())
    number = input()

    cnt = 0
    max_count = 0

    for i in number:
        if i == '1':
            cnt += 1
            if cnt > max_count:
                max_count = cnt
        else:
            if cnt > max_count:
                max_count = cnt
            cnt = 0

    print('#{} {}'.format(t, max_count))