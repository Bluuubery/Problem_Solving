import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221225 3649 로봇 프로젝트

# 정답코드

while True:
    try:
        X = int(input())
        X *= 10000000

        N = int(input())

        lego = list(int(input()) for _ in range(N))
        lego.sort()

        ans = []

        start, end = 0, N - 1

        while start < end:
            if lego[start] + lego[end] < X:
                start += 1
            elif lego[start] + lego[end] > X:
                end -= 1
            else:
                ans = [lego[start], lego[end]]
                break

        if ans:
            print(f'yes {ans[0]} {ans[1]}')
        else:
            print('danger')
    except:
        break