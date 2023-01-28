def solution(people:list, limit:int):

    people.sort(reverse=True)
    # people_down = list(reversed(people))
    
    left = 0
    right = len(people) - 1

    answer = 0

    while True:

        weight = 0

        if left > right:
            break
        
        weight += people[left]

        while True:
            
            if weight + people[right] > limit:
                break

            if left >= right:
                break

            weight += people[right]
            right -=1
        
        left += 1
        answer += 1
        
    return answer