import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220131 1806 부분합

# 정답코드

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
right = 0
sum_num = numbers[0]

min_len = sys.maxsize

while True:
    
    if sum_num >= M:
        sum_num -= numbers[left]
        min_len = min(min_len, right - left + 1)
        
        left += 1

    else:
        right += 1

        if right == N:
            break

        sum_num += numbers[right]
    
    # print(left, right, sum_num, min_len)


if min_len == sys.maxsize:
    print(0)
else:
    print(min_len)