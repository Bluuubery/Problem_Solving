# 220905 2170 선 긋기

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())

# line: 선분의 좌표를 담을 리스트
line = []
for _ in range(N):
    # start, end: 좌표의 시작과 끝
    start, end = map(int, input().split())
    # 만약 순서가 뒤바뀌어있으면 바꿔서 넣어준다.
    if start > end:
        start, end = end, start
    line.append((start, end))

# 시작점과 끝점 순으로 정렬
line.sort(key=lambda x:(x[0], x[1]))

# start: 선분의 시작점, end: 선분의 끝점
start = line[0][0]
end = line[0][1]
# line_length: 선분의 길이
line_length = end - start

for i in range(1, N):

    # 선분이 이어지는 경우
    if line[i][0] < end:
        # 끝점이 더 길면 길이를 추가해주고 끝점을 갱신한다.
        if line[i][1] > end:
            line_length += line[i][1] - end
            end = line[i][1]

    # 선분이 이어지지 않을 떄
    else:
        # 끊어진 길이만큼 빼준다.
        line_length -= line[i][0] - end
        # 끝점을 연장해주고 갱신해준다.
        line_length += line[i][1] - end
        end = line[i][1]

# 최종 선분의 길이 출력
print(line_length)


 



