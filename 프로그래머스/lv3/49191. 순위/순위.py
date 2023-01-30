def dfs(node, graph, visited):

    visited[node] = 1
    
    for next in graph[node]:

        if visited[next]:
            continue

        visited[next] = 1
        dfs(next, graph, visited)

    return sum(visited)


def solution(n, results):
    answer = 0

    win_graph = [[] for _ in range(n + 1)]
    lose_graph = [[] for _ in range(n + 1)]

    for result in results:
        win, lose = result

        win_graph[win].append(lose)
        lose_graph[lose].append(win)
    
    for i in range(1, n + 1):
        visited = [0 for _ in range(n + 1)]
        win_cnt = dfs(i, win_graph, visited) - 1


        visited = [0 for _ in range(n + 1)]
        lose_cnt = dfs(i, lose_graph, visited) - 1

        if win_cnt + lose_cnt == n - 1:
            answer += 1


    return answer