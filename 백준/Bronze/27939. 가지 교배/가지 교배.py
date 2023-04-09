import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230408 가지컵 A. 가지교배

# 정답코드

N = int(input())

type_input = list(input().split())

type_dict = dict()

for i in range(N):
    type_dict[i + 1] = type_input[i]

M, K = map(int, input().split())

ans = "P"

for i in range(M):
    ta = list(map(int, input().split()))
    
    for idx in ta:
        if type_dict[idx] == 'P':
            break
    else:
        ans = "W"

print(ans)
