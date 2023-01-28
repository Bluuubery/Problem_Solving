
def solution(m:int, n:int, puddles:list):
    
    answer = 0

    # dp 테이블 선언 및 초기화
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # 웅덩이
    for puddle in puddles:
        c, r = puddle
        
        r -= 1
        c -= 1

        dp[r][c] = -1


    # dp 테이블 위아래 값으로부터 이동 가능 여부 확인해서 더해나가기
    for r in range(n):
        for c in range(m):

            # 집
            if r == 0 and c == 0:
                dp[r][c] = 1
                continue
            
            # 웅덩이 건너뛰기
            if dp[r][c] == -1:
                continue
            
            # 아래로 가는 경로
            if 0 <= r - 1 < n:
                if dp[r - 1][c] != -1:
                    dp[r][c] += dp[r - 1][c]
            
            # 오른쪽으로 가는 경로
            if 0 <= c - 1 < m:
                if dp[r][c - 1] != -1:
                    dp[r][c] += dp[r][c - 1]

    answer = dp[-1][-1] % 1000000007

    return answer