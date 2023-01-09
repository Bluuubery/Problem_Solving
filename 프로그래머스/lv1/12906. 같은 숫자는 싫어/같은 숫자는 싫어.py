def solution(arr):
    answer = []
    for num in arr:
        if answer and answer[-1] == num:
            continue
        answer.append(num)

    return answer