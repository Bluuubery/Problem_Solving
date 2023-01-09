from collections import deque


def solution(progresses, speeds):

    progresses = deque(progresses)
    speeds = deque(speeds)

    answer = []

    done = 0
    
    while True:
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses and progresses[0] >= 100:

            cnt = 0

            while True:

                if not progresses:
                    break

                if progresses[0] < 100:
                    break

                progresses.popleft()
                speeds.popleft()

                cnt += 1

            done += cnt
            answer.append(cnt)

        if not progresses:
            break
        

    return answer