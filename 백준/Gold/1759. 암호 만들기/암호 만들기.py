# 220916 1759 암호만들기

# 정답코드

import sys
input = sys.stdin.readline

# L: 암호 길이, C: 알파벳 개수 
L, C = map(int, input().split())
char = list(input().strip().split())
char.sort()

# vowel: 모음음 판별하기 위한 리스트
vowel = ['a', 'e', 'i', 'o', 'u']

# password: 생성된 암호를 담을 리스트 
password = []

# result: 암호들을 담을 리스트
result = []


# 생성된 암호문이 조건에 맞는지 파악하는 함수
def count_v_c(password=list):
    cnt_v = 0
    cnt_c = 0

    for i in password:
        if i in vowel:
            cnt_v += 1
        else:
            cnt_c += 1

    if cnt_v >= 1 and cnt_c>= 2:
        return True
    else: 
        return False


# 백트래킹으로 암호 생성하는 함수
def back_tracking(current):

    # 암호문의 길이가 L이 됐을 때
    if len(password) == L:

        # 해당 암호문이 조건에 맞으면 result에 담아준다.
        if count_v_c(password):
            result.append(''.join(password))
        return
    
    # 백트래킹으로 L길이의 암호 생성
    for i in range(current, C):
        password.append(char[i])

        back_tracking(i + 1)

        password.pop()


# 암호 생성
back_tracking(0)

# 암호 출력
for pw in result:
    print(pw)
