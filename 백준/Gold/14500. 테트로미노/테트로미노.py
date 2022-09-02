# 220903 14500 테트리미노

# 정답코드

import sys
input = sys.stdin.readline


# 단방향 테트로미노 검증 함수
# 기본 배열에 한번, 90도 회전 시킨 배열에 또 한번 적용해서 결과를 구한다.
def tetromino(arr, N, M, max_sum):

    # num_sum: 블럭 숫자의 합계

    # (ㅡ)자 블럭 검증
    for r in range(N):
        for c in range(M - 3):
            num_sum = sum(arr[r][c:c + 4])
            # 최댓값 비교해주면서 갱신
            if num_sum > max_sum:
                max_sum = num_sum

    # 사각형 블럭 검증
    for r in range(N - 1):
        for c in range(M - 1):
            num_sum = arr[r][c] + arr[r + 1][c] + arr[r][c + 1] + arr[r + 1][c + 1]
            if num_sum > max_sum:
                max_sum = num_sum

    # L, ㅗ, z자 블럭 검증
    for r in range(N - 1):
        for c in range(M - 2):
            # 6(2 * 3)칸짜리 배열 잘라내기
            mini_arr = [arr[r][c:c + 3], arr[r + 1][c:c + 3]]

            # L, ㅗ자 블럭 검증
            # temp: 수들의 합을 담을 임시 배열
            temp = []
            # 잘라낸 6칸짜리 배열에서 (밑/위)에 3칸에 (밑/위)에 한칸씩 각각 더한다.
            for i in range(3):
                num_sum = sum(mini_arr[0]) + mini_arr[1][i]
                temp.append(num_sum)
                num_sum = sum(mini_arr[1]) + mini_arr[0][i]
                temp.append(num_sum)
            # 최댓값만을 뽑아내서 현재 최댓값과 비교해서 갱신
            if max(temp) > max_sum:
                max_sum = max(temp)
            
            # z자 블럭 검증
            # temp: 수들의 합을 담을 임시 배열
            temp = []
            # (밑/위)행 0, 1번 원소 + (밑/위)행 1, 2번 원소
            num_sum = sum(mini_arr[0][0:2]) + sum(mini_arr[1][1:3])
            temp.append(num_sum)
            num_sum = sum(mini_arr[1][0:2]) + sum(mini_arr[0][1:3])
            temp.append(num_sum)
            # 최댓값만을 뽑아내서 현재 최댓값과 비교해서 갱신
            if max(temp) > max_sum:
                max_sum = max(temp)

    # 최댓값을 반환한다.
    return max_sum


# N, M: 배열의 크기, arr: 배열 
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# first_max: 배열 arr 테트로미노(단방향)의 최댓값
first_max = tetromino(arr, N, M, 0)

# arr_rotate: 배열 arr을 시계방향으로 90도 회전시킨 배열
arr_rotate = list(map(list, zip(*arr[::-1])))

# ans: first_max에서 이어서 검증한 arr_rotate 테트리미노의 최댓값
ans = tetromino(arr_rotate, M, N, first_max)

print(ans)

    

