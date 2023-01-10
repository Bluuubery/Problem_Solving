def solution(prices):
    answer = []
    
    for i in range(len(prices) - 1):
        cnt = 1
        for j in range(i + 1, len(prices) - 1):
            if prices[j] < prices[i]:
                break
            cnt += 1
        answer.append(cnt)
    
    answer.append(0)
            
    return answer