def solution(triangle):
    
    answer = 0

    N = len(triangle)

    
    # dp 테이블 초기화
    dp = [[0 for _ in range(i)] for i in range(N + 1)]

    dp[1] = triangle[0]


    triangle = [0] + triangle

    for level in range(2, N + 1):
        for idx in range(level):
            
            if idx == 0:
                dp[level][idx] = dp[level - 1][idx] + triangle[level][idx]

            elif idx == level - 1:
                dp[level][idx] = dp[level - 1][idx - 1] + triangle[level][idx]
            
            else:
                dp[level][idx] = max(dp[level - 1][idx - 1] + triangle[level][idx], dp[level - 1][idx] + triangle[level][idx])


    answer = max(dp[-1])


    return answer