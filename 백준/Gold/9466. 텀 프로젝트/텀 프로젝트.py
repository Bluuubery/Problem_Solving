import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
sys.setrecursionlimit(10**6)

# 221001 9466 텀 프로젝트

# 정답코드

T = int(input())



def dfs(idx):
    global cnt

    team.append(idx)
    visited[idx] = 1

    if not visited[students[idx]]:

        dfs(students[idx])

    else:
        if students[idx] in team:
            cnt += len(team[team.index(students[idx]):])
            
        return





for _ in range(T):
    N = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(N + 1)]
    team = [0 for _ in range(N + 1)]
    cnt = 0
    
    for idx in range(1, N + 1):
        if not visited[idx]:
            team = []
            dfs(idx)
    
    print(N - cnt)