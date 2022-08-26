# 출발점이 주어졌을 때 해당 노드를 출발점으로 하는 DFS 구현
def dfs(s):
    global visited
    global stack

    # 출발점 방문
    visited[s] = 1

    while True:
        # 인접노드 탐색
        for w in adj_dict[s]:
            # 미방문 인접노드 있을 시 해당 노드로 이동
            if visited[w] == 0:
                stack.append(s)
                s = w
                visited[w] = 1
                break
        # 미방문 인접노드 없을 시
        else:
            # 미방문 인접노드가 있는 노드까지 거슬러 올라가서 다시 탐색한다.
            if stack:
                s = stack.pop()
            # 경로에 가능한 모든 노드를 탐색했을 경우 탐색을 중단한다.
            else:
                break
    return


for _ in range(10):
    T, E = map(int, input().split())
    graph = list(map(int, input().split()))

    adj_dict = {i: [] for i in range(100)}

    for i in range(0, E * 2, 2):
        adj_dict[graph[i]].append(graph[i + 1])

    visited = [0] * 100
    stack = []

    dfs(0)

    if visited[99]:
        print('#{} 1'.format(T))
    else:
        print('#{} 0'.format(T))