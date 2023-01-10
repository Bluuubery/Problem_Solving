import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)

    def mix(scoville):        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + second * 2)
        
        return scoville

    answer = 0
    
    while True:

                        
        if len(scoville) == 1 and K > scoville[0]:
            answer = -1
            break
        
        if scoville[0] >= K:
            break
        
        scoville = mix(scoville)
        
        answer += 1


    return answer

