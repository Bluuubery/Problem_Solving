def solution(answers):
    answer = []
    
    supo_1 = [1, 2, 3, 4, 5] * 2000
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    cnt_1, cnt_2, cnt_3 = 0, 0, 0
    
    for i in range(len(answers)):
        ans = answers[i]
        
        if ans == supo_1[i]:
            cnt_1 += 1
        
        if ans == supo_2[i]:
            cnt_2 += 1
            
        if ans == supo_3[i]:
            cnt_3 += 1
        
    max_score = max([cnt_1, cnt_2, cnt_3])
        
    temp_list =  list(enumerate([cnt_1, cnt_2, cnt_3], start = 1))
                      
    for (idx, score) in temp_list:
        if score == max_score:
            answer.append(idx)
    
    return answer