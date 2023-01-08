from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    
    for c in clothes:
        clothes_dict[c[1]] += 1
    
    answer = 1
    
    for type in clothes_dict:
        answer *= (clothes_dict[type] + 1)
    
    answer -= 1
    
    return answer