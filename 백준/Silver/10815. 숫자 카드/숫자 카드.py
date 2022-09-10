# 220910 10815 숫자 카드

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

K = int(input())
targets = list(map(int, input().split()))

cards.sort()

def binary_search(target, start, end):
    mid = (start + end) // 2

    if start >  end:
        print(0, end=' ')
        return

    if cards[mid] == target:
        print(1, end=' ')
        return
    elif cards[mid] > target:
        binary_search(target, start, mid - 1)
    else:
        binary_search(target, mid + 1, end)

for target in targets:
    binary_search(target, 0, N - 1)