import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221218 5635 생일

# 정답코드

N = int(input())

students = [list(map(str, input().split())) for _ in range(N)]

students.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(students[-1][0])
print(students[0][0])