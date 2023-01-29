def solution(n, costs:list):
    answer = 0

    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def merge(x, y):
        x = find(x)
        y = find(y)

        if x < y:
            parent[y] = x
        else:
            parent[x] = y

        return
    
    costs.sort(key = lambda x: x[2])

    for edge in costs:
        node1, node2, cost = edge
        if find(node1) != find(node2):
            merge(node1, node2)
        
            answer += cost

    return answer
