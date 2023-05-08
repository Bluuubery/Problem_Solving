import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230508 1451 나무꾼 이다솜

# 정답코드

N, C, W = map(int, input().split())

trees = []

for _ in range(N):
    trees.append(int(input()))

max_tree = max(trees)

answer = 0

for i in range(1, max_tree + 1):
    temp = 0
    for tree in trees:
        sale = (tree // i) * W * i
        cost = C * (tree // i if tree % i else tree // i - 1)
        profit = sale - cost
        if profit > 0:
            temp += profit

    answer = max(answer, temp)

print(answer)