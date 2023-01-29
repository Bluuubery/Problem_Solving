from collections import deque
from sys import maxsize


def bfs(start: int, graph: list, visited: list):

    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        current = queue.popleft()

        for next in graph[current]:

            if visited[next]:
                continue

            visited[next] = 1
            queue.append(next)
    
    return sum(visited)


def solution(n:int, wires:list):
    answer = maxsize

    for i in range(len(wires)):

        cut_wire = wires[:]
        cut_wire.remove(wires[i])

        graph = [[] for _ in range(n + 1)]
        
        for node1, node2 in cut_wire:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = [0 for _ in range(n + 1)]
        
        cnt = 0
        for edge in graph:
            if edge:
                cnt = bfs(edge[0], graph, visited)
                break

        diff = abs(n - cnt - cnt)

        
        answer = min(answer, diff)


    return answer