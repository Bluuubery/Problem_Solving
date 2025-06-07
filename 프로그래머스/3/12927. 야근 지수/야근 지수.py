import heapq

def solution(n, works):
    answer = 0
    # 1) works 최대힙
    max_heap = []
    for w in works:
        heapq.heappush(max_heap, (-w, w))
    
    # 2) n만큼 힙의 최댓값에서 빼고 다시 넣기
    for i in range(n):
        t1 = heapq.heappop(max_heap)
        l1 = list(t1)
        # 일 다 했을 경우 break
        if l1[1] == 0: break
        
        l1[0] += 1
        l1[1] -= 1
        heapq.heappush(max_heap, tuple(l1))

    #3) 결과 구하기
    for work_tuple in max_heap:
        answer += work_tuple[1]**2    
        
    return answer