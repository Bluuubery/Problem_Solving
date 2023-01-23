def solution(n, lost, reserve):

    answer = n

    reserve.sort()

    visited = []

    for r in reserve:

        if r in lost:
            lost.remove(r)
            visited.append(r)

    for r in reserve:

        if r in visited:
            continue

        front = r - 1
        back = r + 1

        if front in lost:
            lost.remove(front)
        elif back in lost:
            lost.remove(back)

    answer -= len(lost)
    
    return answer
