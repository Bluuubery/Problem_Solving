import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220131 1806 부분합

# 정답코드

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 투포인터
left = 0
right = 0

# 부분합
sum_num = numbers[0]

# 최소길이 선언 및 초기화
min_len = sys.maxsize

while True:
    
    # 부분합이 M보다 클 경우 수열 길이 줄이기
    if sum_num >= M:
        sum_num -= numbers[left]
        min_len = min(min_len, right - left + 1)
        
        left += 1

    # 작을 경우 수열 길이 늘리기
    else:
        right += 1

        # 탐색 완료
        if right == N:
            break

        sum_num += numbers[right]
    

if min_len == sys.maxsize:
    print(0)
else:
    print(min_len)