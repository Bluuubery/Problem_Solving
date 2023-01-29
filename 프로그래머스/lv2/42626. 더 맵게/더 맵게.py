import heapq

def solution(scoville, K):
    
    # 우선순위큐
    heapq.heapify(scoville)
    
    # 섞기
    def mix(scoville):    
        # 가장 덜 매운 2개 우선순위큐로 추출
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 섞기
        heapq.heappush(scoville, first + second * 2)
        
        return scoville

    answer = 0
    
    while True:

        # 음식이 하나밖에 남지 않았거나  
        if len(scoville) == 1 and K > scoville[0]:
            answer = -1
            break
        
        if scoville[0] >= K:
            break
        
        scoville = mix(scoville)
        
        answer += 1


    return answer

