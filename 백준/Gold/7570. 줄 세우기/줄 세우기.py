import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220921 7570 줄세우기

# 정답코드

N = int(input())
children = list(map(int, input().split()))

lis = [1 for _ in range(max(children) + 1)]
children_set = set()
for i in range(N):
    children_set.add(children[i])
    if children[i] - 1 in children_set:
        lis[children[i]] = lis[children[i] - 1] + 1
    
print(N - max(lis))