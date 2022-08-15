# 220815 1181 단어 정렬

import sys

input = sys.stdin.readline

N = int(input())

words = []

for _ in range(N):
    words.append(input().rstrip())

# set을 이용해 중복을 제거해준다.
words = list(set(words))

# 람다를 이용해 단어의 길이를 첫번째 키로, 사전순으로 두번째 키로 정렬한다.
words.sort(key= lambda x: (len(x), x))

for word in words:
    print(word)