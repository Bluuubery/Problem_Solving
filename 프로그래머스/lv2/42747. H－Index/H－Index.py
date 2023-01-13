def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx in range(len(citations)):
        if citations[idx] >= idx + 1:
            answer = idx + 1
    
    return answer
