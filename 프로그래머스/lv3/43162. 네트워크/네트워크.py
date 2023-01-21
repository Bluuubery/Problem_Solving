def solution(n, computers):

    answer = 0
    visited = [0 for _ in range(n)]

    def dfs(node):

        visited[node] = 1

        for next in range(n):

            if computers[node][next] and not visited[next]:
                
                dfs(next)

    for i in range(n):

        if not visited[i]:
            dfs(i)

            answer += 1


    return answer

