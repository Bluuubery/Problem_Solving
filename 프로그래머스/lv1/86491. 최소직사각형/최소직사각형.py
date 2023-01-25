def solution(sizes):
    
    sizes = list(map(sorted, sizes))
    x = max(sizes, key = lambda x: x[0])
    y = max(sizes, key = lambda x: x[1])
    
    answer = x[0] * y[1]

    return answer