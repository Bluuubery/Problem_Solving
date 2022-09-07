# 220907 1253 좋다

# 정답코드

import sys
input = sys.stdin.readline

# N: 숫자의 갯수, numers: 숫자들을 담은 리스트
N = int(input())
numbers = list(map(int, input().split()))

# 수열을 정렬해준다.
numbers.sort()

# good: 좋은 숫자의 갯수
good = 0
# 투포인터로 범위 좁혀가면서 탐색
for i in range(N):

    # target: 검증할 숫자를 리스트에서 빼낸다.
    target = numbers.pop(i)
    # start: 시작 포인터, end: 끝 포인터
    start = 0
    end = N - 2

    # 포인터가 교차되기 전까지 탐색
    while end > start:
        # 좋은 숫자인 경우
        if numbers[start] + numbers[end] == target:
            good += 1
            break
        # 두 숫자의 합이 목표 숫자보다 클 경우 end 포인터를 좌로 한 칸 이동
        elif numbers[start] + numbers[end] > target:
            end -= 1
        # 두 숫자의 합이 목표 숫자보다 작을 경우 start 포인터를 우로 한 칸 이동
        else:
            start += 1

    # 탐색을 마쳤으면 숫자를 다시 리스트에 넣는다.
    numbers.insert(i, target)

# 좋은 숫자 갯수 출력
print(good)