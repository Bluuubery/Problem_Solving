# 220820 2559 수열

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

temperature = list(map(int, input().split()))

# 초기 max값을 첫 구간합으로 설정한다.(-99999하면 첫 값이 비교가 안됨)
max_temp = sum(temperature[0:K])

# 첫 구간합
sum_temp = sum(temperature[0:K])
# 투 포인터(start: 탐색 구간의 첫 값, end: 탐색 구간의 끝 값 다음 값)
start = 0
end = K

while True:
    # 포인터가 끝에 도달하면 탐색 중단
    if end == N:
        break

    # 구간합 구하기
    sum_temp = sum_temp - temperature[start] + temperature[end]
    # 최댓값 갱신
    if sum_temp > max_temp:
        max_temp = sum_temp

    # 투 포인터 이동
    start += 1
    end += 1

print(max_temp)
