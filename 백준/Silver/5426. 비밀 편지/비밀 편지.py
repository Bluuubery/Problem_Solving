import sys, os, io, atexit
import math

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221211 5426 비밀편지

# 정답코드

T = int(input())

for _ in range(T):
    secret = input()

    square_len = int(math.sqrt(len(secret)))

    arr = [['' for _ in range(square_len)] for _ in range(square_len)]

    for idx, char in enumerate(secret):
        arr[idx//square_len][idx%square_len] = char
    
    arr = list(map(list, zip(*arr)))[::-1]

    ans = ''
    
    for lst in arr:
        ans += ''.join(lst)
    
    print(ans)
