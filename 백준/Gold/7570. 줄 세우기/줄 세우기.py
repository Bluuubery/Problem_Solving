import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220921 7570 줄세우기

# 정답코드

# N: 아이들 명 수
N = int(input())
# children: 아이들 번호
children = list(map(int, input().split()))

# lis: 연속적으로 증가하는 부분수열의 길이(1로 초기화)
lis = [1 for _ in range(max(children) + 1)]
# children_set: 아이들의 번호를 담을 셋
children_set = set()

for i in range(N):
    # 아이의 번호를 셋에 넣는다.
    children_set.add(children[i])
    # 직전 번호가 셋에 존재하면 lis 길이 갱신
    if children[i] - 1 in children_set:
        lis[children[i]] = lis[children[i] - 1] + 1

# 아이들 전체 명 수에서 가장 긴 연속적으로 증가하는 부분수열의 길이를 빼준다.
print(N - max(lis))