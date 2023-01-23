def solution(name):
    answer = 0

    # 변환 횟수
    for char in name:
        answer += min(ord(char) - 65, 90 - ord(char) + 1)
    
    
    # 최단 경로

    min_move = len(name) - 1

    for i in range(len(name) - 1):
        
        next  = i + 1

        while True:
            
            # 종료 조건
            if next >= len(name):
                break
            
            if name[next] != 'A':
                break

            next += 1
        
        min_move = min(min_move, i * 2 + len(name) - next, i + 2 * (len(name) - next))

    answer += min_move

    return answer