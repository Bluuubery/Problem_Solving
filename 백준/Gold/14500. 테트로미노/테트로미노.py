# 220903 14500 테트리미노

# 정답코드

import sys
input = sys.stdin.readline


def tetromino(arr, N, M, max_sum):

    # (ㅡ)자 블럭 검증
    for r in range(N):
        for c in range(M - 3):
            num_sum = sum(arr[r][c:c + 4])
            # print(f'일자 블럭: {num_sum}')
            if num_sum > max_sum:
                max_sum = num_sum

    # 사각형 블럭 검증
    for r in range(N - 1):
        for c in range(M - 1):
            num_sum = arr[r][c] + arr[r + 1][c] + arr[r][c + 1] + arr[r + 1][c + 1]
            # print(f'사각 블럭: {num_sum}')
            if num_sum > max_sum:
                max_sum = num_sum

    # L, ㅗ, z자 블럭 검증
    for r in range(N - 1):
        for c in range(M - 2):
            # 6칸짜리 배열 잘라내기
            mini_arr = [arr[r][c:c + 3], arr[r + 1][c:c + 3]]

            # L, ㅗ자 블럭 검증
            # temp: 수들의 합을 담을 임시 배열
            temp = []
            for i in range(3):
                num_sum = sum(mini_arr[0]) + mini_arr[1][i]
                temp.append(num_sum)
                num_sum = sum(mini_arr[1]) + mini_arr[0][i]
                temp.append(num_sum)
            # 최댓값만을 뽑아내서 현재 최댓값과 비교해서 갱신
            if max(temp) > max_sum:
                max_sum = max(temp)
            
            # z자 블럭 검증
            temp = []
            num_sum = sum(mini_arr[0][0:2]) + sum(mini_arr[1][1:3])
            temp.append(num_sum)
            num_sum = sum(mini_arr[1][0:2]) + sum(mini_arr[0][1:3])
            temp.append(num_sum)
            # print(f'z자 블럭: {temp}')

            # 최댓값만을 뽑아내서 현재 최댓값과 비교해서 갱신
            if max(temp) > max_sum:
                max_sum = max(temp)

    return max_sum

    
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

first_max = tetromino(arr, N, M, 0)

arr_rotate = list(map(list, zip(*arr[::-1])))

ans = tetromino(arr_rotate, M, N, first_max)

print(ans)

    

