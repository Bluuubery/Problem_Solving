import heapq

def solution(jobs):
    answer = 0

    idx = 0
    time = 0 

    cnt = 0

    jobs.sort()

    heap = []
    
    while len(jobs) > cnt:

        if idx < len(jobs):
            for i in range(idx, len(jobs)):
                if jobs[i][0] <= time:
                    heapq.heappush(heap, jobs[i][::-1])
                    idx = i + 1
        
        if heap:
            current = heapq.heappop(heap)
            time += current[0]
            answer += time - current[1]
            cnt += 1
        else:
            time +=1
            
    answer //= len(jobs)

    return answer 