import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230201 1522 문자열 교환

# 정답코드

string = input()

N = len(string)
cnt_a = string.count('a')

ans = 1000


string += string[:-1]


for i in range(N):
    sub_string = string[i:i+cnt_a]
    
    ans = min(ans, sub_string.count('b'))

print(ans)