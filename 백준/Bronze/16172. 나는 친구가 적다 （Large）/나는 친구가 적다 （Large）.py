import sys, os, io, atexit
import re

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221218 16172 나는 친구가 적다

# 정답코드

textbook = input()
keyword = input()

str = re.sub('[0-9]', '', textbook)

if keyword in str:
    print(1)
else:
    print(0)