T = int(input())

for t in range(1, T + 1):
    N = int(input())
    seen = 0
    sheep = N

    while True:
        for i in str(sheep):
            seen |= 1 << int(i)

        if seen == (1 << 10) - 1:
            break

        sheep += N

    print('#{} {}'.format(t, sheep))