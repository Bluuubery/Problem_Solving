import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230131 12919 A와 B 2

# 정답코드
start = str(input())
target = str(input())


def recursion(word):

    if len(word) == len(start):

        if word == start:
            print(1)
            exit()
            
        return


    if word[0] == 'B':

        if word[-1] == 'A':

            recursion(word[:-1])
            recursion(word[::-1][:-1])

        else:

            recursion(word[::-1][:-1])

    else:

        if word[-1] == 'A':

            recursion(word[:-1])

recursion(target)

print(0)