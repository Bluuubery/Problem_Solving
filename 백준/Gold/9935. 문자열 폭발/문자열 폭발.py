import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221002 9935 문자열 폭발

# 정답코드

stack = []
string = input()
explode = input()

N = len(explode)
end = explode[-1]

for char in string:
    stack.append(char)


    if char == end and ''.join(stack[-N:]) == explode:
        for _ in range(N):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')