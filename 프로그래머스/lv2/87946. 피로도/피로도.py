from itertools import permutations

def solution(k, dungeons):
    answer = 0
    N = len(dungeons)
    
    for perm in permutations(dungeons):
        cnt = 0
        left = k
        
        for i in range(N):
            
            energy = perm[i]
            if left >= energy[0]:
                left -= energy[1]
                cnt += 1
                
        answer = max(cnt, answer)
    
    return answer