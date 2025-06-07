def solution(numbers, target):
    answer = 0
    N = len(numbers)

    def dfs(depth, result):
        nonlocal answer

        if depth == N:
            if result == target:
                answer += 1
            return
        
        dfs(depth + 1, result + numbers[depth])
        dfs(depth + 1, result - numbers[depth])
    
    dfs(0, 0)
    
    return answer