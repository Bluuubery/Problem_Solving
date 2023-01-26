def solution(brown, yellow):
    
    # 사각형 둘레의 절반
    perimeter_half = (brown +4) // 2
    
    # 사각형 가로 세로 길이 경우의 수 완전탐색
    for i in range(3, perimeter_half//2 + 1):
        
        j = perimeter_half - i
        
        if (i - 2) * (j - 2) == yellow:
            
            answer =  [j, i]
            break
    
    
    return answer