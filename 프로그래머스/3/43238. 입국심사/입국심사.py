def solution(n, times):

    answer = 0

    
    left = 1
    right = max(times) * n

    while True:

        # cnt: 검사 받은 인원 수
        cnt = 0

        # mid: 검사 시간
        mid = (left + right) // 2

        if left > right:
            break
        
        # 각 심사관들이 검사하는 인원수 더해주기
        for time in times:
            cnt += mid // time

        # 이분 탐색
        if cnt >= n:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1


    return answer