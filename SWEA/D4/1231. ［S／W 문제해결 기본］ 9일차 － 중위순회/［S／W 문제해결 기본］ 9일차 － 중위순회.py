# 220913
# 1231 중위순회

# 정답코드

# import sys

# sys.stdin = open('input.txt', 'r')


def in_order(node):
    if node <= N:
        in_order(node * 2)
        print(tree[node], end='')
        in_order(node *2 + 1)



for t in range(1, 11):
    N = int(input())

    tree = [[] for _ in range(N + 1)]

    for _ in range(N):
        edge_info = list(input().split())
        tree[int(edge_info[0])] = edge_info[1]
    
    print('#{}'.format(t), end=' ')
    in_order(1)
    print()