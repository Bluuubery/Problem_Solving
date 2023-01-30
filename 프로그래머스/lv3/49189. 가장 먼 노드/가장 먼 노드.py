from collections import deque


def bfs(node, graph, n):
    visited = [0 for _ in range(n + 1)]

    queue = deque()
    queue.append(node)
    visited[node] = 1

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            if visited[next]:
                continue

            queue.append(next)
            visited[next] = visited[node] + 1
    
    return visited




def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    
    for e in edge:
        node1, node2 = e
        graph[node1].append(node2)
        graph[node2].append(node1)

    visited = bfs(1, graph, n)
    
    answer = visited.count(max(visited))

    return answer