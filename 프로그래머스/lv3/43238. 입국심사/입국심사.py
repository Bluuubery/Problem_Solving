def solution(n, times):

    answer = 0


    left = 1
    right = max(times) * n

    while True:
        cnt = 0

        mid = (left + right) // 2

        if left > right:
            break

        for time in times:
            cnt += mid // time

        
        if cnt >= n:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1



    return answer