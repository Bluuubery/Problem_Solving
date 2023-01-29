import heapq


def solution(operations):
    answer = [0, 0]
    heap = []
    
    
    for operation in operations:
        
        # 삽입 연산자
        if operation[0] == 'I':
            heapq.heappush(heap, int(operation[2:]))
        
        # 삭제연산자
        else:
            if not heap:
                continue
            
            # 최솟값 삭제
            if operation[2] == '-':
                heapq.heappop(heap)
            # 최댓값 삭제
            else:
                heap.remove(max(heap))
    
    # 정답 반환
    if heap: 
        answer = [max(heap), min(heap)]

    return answer