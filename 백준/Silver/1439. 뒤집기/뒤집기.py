# 220904 1439 뒤집기

# 정답코드

import sys
input = sys.stdin.readline

S = input().strip()

# str_0: 연속된 0으로 구성된 문자열의 개수, str_1: 연속된 1로 구성된 문자열의 개수
if S[0] == '0':
    str_0 = 1
    str_1 = 0
else:
    str_0 = 0
    str_1 = 1

# 문자가 바뀌면 다음에 오는 문자에 따라 문자열을 세준다.
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i + 1] == '0':
            str_0 += 1
        else:
            str_1 += 1

# 두 문자열 중 적은 것의 개수 출력
print(min(str_0, str_1))