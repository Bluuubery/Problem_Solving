# 220913 15681 트리와 쿼리

# 정답코드

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# N: 정점 수, R: 루트 번호, Q: 쿼리 수
N, R, Q = map(int, input().split())

tree_no_root = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    node_1, node_2 = map(int, input().split())
    tree_no_root[node_1].append(node_2)
    tree_no_root[node_2].append(node_1)

query =[]
for _ in range(Q):
    query.append(int(input()))


def set_root(current_node, parent):
    
    for node in tree_no_root[current_node]:
        if node != parent:
            child[current_node].append(node)
            set_root(node, current_node)
    
    return 


def count_subtree(current_node):
    global size
    size[current_node] = 1
    for node in child[current_node]:
        count_subtree(node)
        size[current_node] += size[node]

    return 


child = [[] for _ in range(N + 1)]
set_root(R, -1)

size = [0 for _ in range(N + 1)]
count_subtree(R)
# print(size)

for i in range(Q):
    print(size[query[i]])