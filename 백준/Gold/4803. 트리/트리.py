# 220913 4803 트리

# 정답코드

import sys
input = sys.stdin.readline


# 트리 여부 판별 dfs 함수
def dfs(node, parent):
    # 방문 표시
    visited[node] = 1

    for child in graph[node]:
        # 방문하고자하는 노드를 이미 방문했을 경우
        if visited[child] == 1:
            # 해당 노드가 부모 노드가 아닌 경우 사이클이므로 False 반환
            if child != parent:
                return False

        # 그 외에는 계속 dfs 탐색
        if visited[child] == 0:
            # 탐색 도중 사이클 발생했을 경우 False 반환
            if not dfs(child, node):
                return False
    
    # 검증 완료 시 True 반환
    return True


# T: 테스트 케이스 번호
T = 1
while True:
    # N: 정점 개수, M: 간선 개수
    N, M = map(int, input().split())
    # 0, 0 입력시 종료
    if N == 0 and M ==0:
        exit()

    # graph: 트리 여부 판별할 그래프
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        parent, child = map(int, input().split())
        graph[parent].append(child)
        graph[child].append(parent)
    
    # visited: 방문 여부 표시 배열
    visited = [0 for _ in range(N + 1)]

    # cnt: 트리 개수 
    cnt = 0
    # 미 방문 노드에서 dfs 실시 후 트리 여부에 따라 cnt 세주기
    for i in range(1, N + 1):
        if visited[i] == 0:
            if dfs(i, 0):
                cnt += 1

    # 트리 개수에 따라 정답 양식 출력
    if cnt > 1:
        print(f'Case {T}: A forest of {cnt} trees.')
    elif cnt == 1:
        print(f'Case {T}: There is one tree.')
    else:
        print(f'Case {T}: No trees.')
    
    # 테스트 케이스 번호 갱신
    T += 1