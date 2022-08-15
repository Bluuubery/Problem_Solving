# 22081 swea 1961 숫자 배열 회전

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    numbers = [list(map(str, input().split())) for _ in range(N)]
    rotate = [['' for _ in range(3)] for _ in range(N)]
    # print(rotate)

    for i in range(N):
        for j in range(N - 1, -1, -1):
            rotate[i][0] += numbers[j][i]

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            rotate[N - i - 1][1] += numbers[i][j]

    for i in range(N - 1, -1, -1):
        for j in range(N):
            rotate[N - i - 1][2] += numbers[j][i]

    print('#{}'.format(t))
    for row in rotate:
        print(*row)
