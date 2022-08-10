# 220810 2630 색종이만들기

import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def paper_cut(a, b, N):
    global white, blue
    cnt = 0
    for i in range(a, a+ N):
        for j in range(b, b + N):
            if paper[i][j]:
                cnt += 1
    if not cnt:
        white += 1
    elif cnt == N**2:
        blue += 1
    else:
        paper_cut(a, b, N // 2)
        paper_cut(a + N // 2, b, N // 2)
        paper_cut(a, b + N // 2, N // 2)
        paper_cut(a + N // 2, b + N // 2, N // 2)

paper_cut(0, 0, n)
print(white)
print(blue)
