import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220920 14888 연산자 끼워넣기

# 정답코드

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_val = -sys.maxsize
min_val = sys.maxsize


def operator(x, y, op):
    if op == 0:
        return x + y
    elif op == 1:
        return x - y
    elif op == 2:
        return x * y
    else:
        if x < 0:
            return -(-x // y)
        else:
            return x // y


def back_tracking(depth, result):
    global max_val, min_val

    if depth == N - 1:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    for i in range(4):
        if operators[i]:
            operators[i] -= 1

            back_tracking(depth + 1, operator(result, numbers[depth + 1], i))

            operators[i] += 1


back_tracking(0, numbers[0])

print(max_val)
print(min_val)
    