# 230122 여행경로


from collections import defaultdict


def solution(tickets):
    
    answer = []
    ticket_dict = defaultdict(list)

    for ticket in tickets:
        ticket_dict[ticket[0]].append(ticket[1])
    
    
    for v in ticket_dict.values():
        v.sort(reverse=True)
    

    stack = ['ICN']

    while stack:

        top = stack[-1]

        if not ticket_dict[top]:
            answer.append(stack.pop())
        else:
            stack.append(ticket_dict[top].pop())

    answer.reverse()

    return answer