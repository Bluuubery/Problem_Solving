# 220904 1439 뒤집기

# 정답코드

S = input()

if S[0] == '0':
    str_0 = 1
    str_1 = 0
else:
    str_0 = 0
    str_1 = 1

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i + 1] == '0':
            str_0 += 1
        else:
            str_1 += 1

print(min(str_0, str_1))