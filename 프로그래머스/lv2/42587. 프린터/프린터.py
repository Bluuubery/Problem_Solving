from collections import deque

def solution(priorities, location):
    printer = deque(enumerate(priorities))
    answer = 0


    while True:
        
        if printer[0][1] == max(printer, key=lambda x:x[1])[1]:

            answer += 1
            idx = printer.popleft()[0]

            if idx == location:
                break

        else:
            printer.append(printer.popleft())

            

    return answer