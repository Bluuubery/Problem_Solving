import heapq


def solution(operations):
    answer = [0, 0]
    heap = []

    for operation in operations:

        if operation[0] == 'I':
            heapq.heappush(heap, int(operation[2:]))
        
        else:
            if not heap:
                continue

            if operation[2] == '-':
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if heap: 
        answer = [max(heap), min(heap)]

    # print(heap, answer)
    return answer