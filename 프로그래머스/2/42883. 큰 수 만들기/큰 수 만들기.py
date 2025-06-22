def solution(number, k):

    answer = ''

    cnt = 0

    stack = []

    for num in number:
        
        while True:

            if not stack:
                break

            if stack[-1] >= num:
                break

            if cnt == k:
                break

            stack.pop()
            cnt += 1

        stack.append(num)
        

    answer = ''.join(stack[:len(number)-k])
    
    return answer