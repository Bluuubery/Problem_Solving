# 22081 swea 1961 숫자 배열 회전

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    # 문자열 형태로 받아준다.
    numbers = [list(map(str, input().split())) for _ in range(N)]
    # 회전된 배열을 담을 빈 배열(문자열)
    rotate = [['' for _ in range(3)] for _ in range(N)]
    # print(rotate)

    # 90도 회전
    for i in range(N):
        for j in range(N - 1, -1, -1):
            rotate[i][0] += numbers[j][i]

    # 180도 회전
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            rotate[N - i - 1][1] += numbers[i][j]

    # 270도 회전
    for i in range(N - 1, -1, -1):
        for j in range(N):
            rotate[N - i - 1][2] += numbers[j][i]

    # 정답을 양식에 맞게 출력해준다.
    print('#{}'.format(t))
    for row in rotate:
        print(*row)
