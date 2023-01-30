# dfs 함수 선언
def dfs(node, graph, visited):

    visited[node] = 1
    
    for next in graph[node]:

        if visited[next]:
            continue

        visited[next] = 1
        dfs(next, graph, visited)

    # 방문한 노드 (승자 or 패자) 수 반환
    return sum(visited) - 1


def solution(n, results):

    answer = 0

    # 승자, 패자 그래프
    win_graph = [[] for _ in range(n + 1)]
    lose_graph = [[] for _ in range(n + 1)]

    for result in results:
        win, lose = result

        win_graph[win].append(lose)
        lose_graph[lose].append(win)


    # 각 노드에 대해서 dfs로 파악된 승자와 패자 수 구하기
    for i in range(1, n + 1):

        # 자신 밑으로 패자의 수
        visited = [0 for _ in range(n + 1)]
        win_cnt = dfs(i, win_graph, visited)

        # 자신 위로 승자의 수
        visited = [0 for _ in range(n + 1)]
        lose_cnt = dfs(i, lose_graph, visited) 

        # 순서가 확정난 경우 
        if win_cnt + lose_cnt == n - 1:
            answer += 1


    return answer