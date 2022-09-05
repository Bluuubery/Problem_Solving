# 220908 1991 트리 순회

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())

tree = dict()
for _ in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]


def pre_order(node):
    if node != '.':
        print(node, end='')
        pre_order(tree[node][0])
        pre_order(tree[node][1])


def in_order(node):
    if node != '.':
        in_order(tree[node][0])
        print(node, end='')
        in_order(tree[node][1])


def post_order(node):
    if node != '.':
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(node, end='')


pre_order('A')
print()
in_order('A')
print()
post_order('A')

