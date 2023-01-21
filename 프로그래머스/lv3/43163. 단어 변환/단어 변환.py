from collections import deque


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    queue = deque()

    queue.append((begin, 0))

    def can_change(word1, word2):
        cnt = 0

        for i in range(len(word1)):

            if word1[i] == word2[i]:
                continue
            
            cnt += 1
        
        if cnt == 1:
            return True
        
        return False

    while queue:

        current, depth = queue.popleft()

        for next in words:
            if can_change(current, next):

                if next == target:
                    answer = depth + 1
                    return answer

                queue.append((next, depth + 1))

    return answer