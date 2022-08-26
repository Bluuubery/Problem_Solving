T = int(input())

for t in range(1, T + 1):
    A, B = map(str, input().split())
    N = len(A)
    M = len(B)

    # 타이핑 횟수와 인덱스를 담을 변수 선언
    cnt = 0
    idx = 0
    while idx < N:
        if A[idx:idx+M] == B:
            cnt += 1
            idx += M
        else:
            cnt += 1
            idx += 1

    print('#{} {}'.format(t, cnt))
