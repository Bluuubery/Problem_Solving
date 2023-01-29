def solution(array, commands):
    answer = []
    
    for command in commands:
        
        # 자르기
        temp = array[command[0] - 1: command[1]]
        
        # 정렬하기
        temp.sort()
        
        # 정답 넣어주기
        answer.append(temp[command[2] - 1])
    
    return answer