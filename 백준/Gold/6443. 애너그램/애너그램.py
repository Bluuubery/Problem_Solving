import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221221 6443 애너그램

# 정답코드


def backtracking(current, str):

    if current == len(word):
        print(str)
        return

    for i in range(len(word)):

        if not visited[i]:

            if str + word[i] not in check_duplicate:

                check_duplicate.add(str + word[i])

                visited[i] = True

                backtracking(current + 1, str+word[i])

                visited[i] = False



N = int(input())

for _ in range(N):
    word = list(input())
    word.sort()

    visited = [False for _ in range(len(word))]

    check_duplicate = set()
    
    backtracking(0, '')
