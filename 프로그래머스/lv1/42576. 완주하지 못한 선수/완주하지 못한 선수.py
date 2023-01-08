def solution(participant, completion):
    answer = ''
    
    ans_dict = {}
    hash_val = 0
    
    for p in participant:
        ans_dict[hash(p)] = p
        hash_val += hash(p)
    
    for c in completion:
        hash_val -= hash(c)

    answer = ans_dict[hash_val]

    return answer