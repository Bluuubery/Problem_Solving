from collections import defaultdict

def solution(survey, choices):
    answer = ''
    
    # 성격 지표 순서
    indicator = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    # 성격 유형 딕셔너리
    personality = defaultdict(int)
    
    # 성격 점수 계산
    N = len(survey)
    
    for i in range(N):
        if choices[i] <= 3:
            personality[survey[i][0]] -= (choices[i] - 4)
        elif choices[i] >= 5:
            personality[survey[i][1]] += (choices[i] - 4)
            
    
    # 성격 유형 검사 결과
    for a, b in indicator:
        if personality[a] >= personality[b]:
            answer += a
        else:
            answer += b
    
    return answer