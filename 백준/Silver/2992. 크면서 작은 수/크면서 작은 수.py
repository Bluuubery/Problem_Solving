import sys, os, io, atexit
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221212 2992 크면서 작은 수

# 정답코드

X = list(input())

arr = list(permutations(X, len(X)))

arr = list(set(arr))

arr.sort()

result = ["".join(num) for num in arr]

idx = result.index("".join(X))

if idx == len(result) - 1:
    print(0)
else:
    print(result[idx + 1])
