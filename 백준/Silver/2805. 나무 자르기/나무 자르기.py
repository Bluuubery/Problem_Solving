# 220911 2805 나무 자르기

# 정답코드

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

tree.sort()


def parametric_search(arr, start, end):
    if start > end:
        print(end)
        return

    mid = (start + end) // 2

    cnt = 0
    for i in range(N):
        if tree[i] > mid:
            cnt += tree[i] - mid


    if cnt >= M:
        parametric_search(arr, mid + 1, end)
    else:
        parametric_search(arr, start, mid - 1)


parametric_search(tree, 0, max(tree))