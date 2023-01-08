from collections import defaultdict

def solution(participant, completion):
    answer = ''
    ans_dict = defaultdict(int)
    
    for p in participant:
        ans_dict[p] += 1
    
    for c in completion:
        ans_dict[c] -= 1
    
    for (k, v) in ans_dict.items():
        if v:
            answer = k
            break

    return answer