# 220814 swea 1204 최빈수 구하기

T = int(input())

for _ in range(T):
    tc = int(input())
    score_list = list(map(int, input().split()))
    # 점수를 key로, 등장횟수를 value로 가지는 딕셔너리 생성
    score_count = {i: 0 for i in range(101)}

    # 딕셔너리에 점수의 등장 횟수를 더해준다.
    for score in score_list:
        score_count[score] += 1

    # 최빈값과 등장횟수를 담을 변수
    mode_score = 0
    max_count = 0

    # 최빈값과 등장횟수를 비교하면서 계속 갱신해준다.
    for k, v in score_count.items():
        # 같을 경우 더 큰 값이기 때문에 >=로 설정해준다.
        if v >= max_count:
            max_count = v
            mode_score = k

    print('#{} {}'.format(tc, mode_score))