# 11721 열 개씩 끊어 출력하기
n = input()

m = len(n)//10 + 1

for i in range(1, m + 1):
    print(n[10*(i-1):10*i])