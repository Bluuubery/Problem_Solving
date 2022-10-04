import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221004 1251 단어 나누기

# 정답코드

string = input()

result = []

for i in range(1, len(string) - 1):
    for j in range(i + 1, len(string)):
        a = string[:i][::-1]
        b = string[i:j][::-1]
        c = string[j:][::-1]
        result.append(a+b+c)

result.sort()
print(result[0])
