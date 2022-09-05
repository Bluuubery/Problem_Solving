# 220905 2170 선 긋기

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())

line = []
for _ in range(N):
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    line.append([start, end])

line.sort(key=lambda x:(x[0], x[1]))
start = line[0][0]
end = line[0][1]
line_length = end - start
for i in range(1, N):
    # 이어질 때
    if line[i][0] < end:
        # 끝점 더 길면 연장
        if line[i][1] > end:
            line_length += line[i][1] - end
            end = line[i][1]
    # 끊어질 떄
    else:
        # 끊어진 거만큼 빼주기
        line_length -= line[i][0] - end
        # 끝점만큼 연장
        line_length += line[i][1] - end
        end = line[i][1]

print(line_length)


 



