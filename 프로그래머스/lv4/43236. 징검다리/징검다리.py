def solution(distance, rocks, n):
    answer = 0


    rocks.sort()
    # print(rocks)
    
    def parametric_search(start, end):
        nonlocal answer

        if start > end:
            answer = end
            return 

        # 징검다리 길이
        mid = (start + end) // 2

        # cnt: 남아있는 바위 개수
        cnt = 0
        # current: 현재 바위
        current = 0

        for i in range(len(rocks)):
            
            # 바위 간격
            dist = rocks[i] - current

            # 최소 징검다리 길이보다 길면 현재 바위와 해당 바위 사이에 다리 설치 (중간 바위 제거)
            if dist >= mid:
                cnt += 1
                current = rocks[i]
                # print(current)

        if len(rocks) - cnt > n:
            # print(start, mid, end, cnt)
            # print()
            parametric_search(start, mid - 1)
        else:
            # print(start, mid, end, cnt)
            # print()
            parametric_search(mid + 1, end)

    parametric_search(0, distance)

    return answer