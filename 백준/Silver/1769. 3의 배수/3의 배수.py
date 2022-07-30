def sum_for_three (n, cnt):
    if len(n) == 1:
        if int(n) % 3:
            print(cnt)
            print('NO')
        else:
            print(cnt)
            print('YES')
    else:
        cnt += 1
        t = 0
        for i in n:
            t += int(i)
        sum_for_three(str(t), cnt)

n = input()
cnt = 0
sum_for_three(n, cnt)