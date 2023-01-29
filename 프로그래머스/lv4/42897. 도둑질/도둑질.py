def solution(money):

    answer = 0

    N = len(money)
    
    # 첫 집을 털거나 안 털거나
    for i in range(2):
        
        # dp 테이블 선언 및 초기화
        dp = [0 for _ in range(N)]

        # i == 0 -> 첫집 0, i == 1 -> 첫집 x
        dp[0] = money[i] if i == 0 else 0
        dp[1] = max(dp[0], money[1])

        # 점화식: dp[j] = max(money[j] + dp[j - 2], dp[j - 1])
        # max(현재집 + 이전이전집, 직전집) 
        for j in range(2, N - 1):
            dp[j] = max(money[j] + dp[j - 2], dp[j - 1])
        
        # 마지막 집
        if i == 0:
            dp[-1] = dp[-2]
        else:
            dp[-1] = max(money[-1] + dp[- 3], dp[- 2])

        
        answer = max(answer, dp[-1])

    return answer