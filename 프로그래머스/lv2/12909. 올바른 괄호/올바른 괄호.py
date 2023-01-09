def solution(s):
    answer = True
    
    stack = []
    
    for char in s:
        
        if not stack: 
            stack.append(char)
            
        else:
            if stack[-1] == '(' and char == ')':
                stack.pop()
            else:
                stack.append(char)
    
    if stack:
        answer = False


    return answer