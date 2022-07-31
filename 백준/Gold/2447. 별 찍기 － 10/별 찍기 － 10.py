n = int(input())
# 별들을 담을 2차원 리스트를 만들어둔다.
temp = [[0 for i in range(n)] for i in range(n)]

def star(n, temp):
    # n = 3일 때
    if n == 3:
        temp[0][:3] = [1, 1, 1]
        temp[1][:3] = [1, 0, 1]
        temp[2][:3] = [1, 1, 1]
    else:
        # n != 3 일 때 재귀 루프를 걸어준다.
        num = n//3
        star(num, temp)
        for i in range(3):
            for j in range(3):
                # 가운데는 비워준다.
                if i == 1 and j == 1:
                    pass
                else:
                    # 바로 왼쪽과 동일한 패턴으로 1(별)을 넣어준다.
                    for k in range(num):
                        temp[num*i + k][num*j : num * (j + 1)] = temp[k][:num]
                        # 구간별 별 출력 확인용 코드
                        # print(temp[num*i + k][num*j : num * (j + 1)]) 

star(n, temp)

# 출력 양식에 맞춰 1일 때 별을, 0일 떄 공백을 출력한다.
for i in temp:
    for j in i:
        if j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
