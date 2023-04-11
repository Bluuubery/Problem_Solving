import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230411 27942 :danceplant:

# 정답코드

dir_dict = {
    "U": [(-1, 0), (0, 0)],
    "D": [(0, 0), (1, 0)],
    "L": [(0, -1), (0, 0)],
    "R": [(0, 0), (0, 1)]
}



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

points = [[N // 2 - 1, N // 2 - 1], [N // 2, N // 2]]
ans = 0
path = ''

flag = True

while True:

    dir = ""
    total = 0
    
    # 위
    if points[0][0] - 1 >= 0:
        up_total = 0
        for i in range(points[0][1], points[1][1] + 1):
            up_total += arr[points[0][0] - 1][i]

        if up_total > 0:
            total = up_total
            dir = "U"

    # 아래
    if points[1][0] + 1 < N:
        down_total = 0
        for i in range(points[0][1], points[1][1] + 1):
            down_total += arr[points[1][0] + 1][i]

        if down_total > total:
            total = down_total
            dir = "D"

    # 왼
    if points[0][1] - 1 >= 0:
        left_total = 0
        for i in range(points[0][0], points[1][0] + 1):
            left_total += arr[i][points[0][1] - 1]

        if left_total > total:
            total = left_total
            dir = "L"

    # 오
    if points[1][1] + 1 < N:
        right_total = 0
        for i in range(points[0][0], points[1][0] + 1):
            right_total += arr[i][points[1][1] + 1]

        if right_total > total:
            total = right_total
            dir = "R"   

    if total == 0:
        break
    
    ans += total
    path += dir
    for i in range(2):
        for j in range(2):
            points[i][j] += dir_dict[dir][i][j]


print(ans)
print(path)