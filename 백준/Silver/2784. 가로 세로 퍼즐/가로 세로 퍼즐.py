import sys, os, io, atexit
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221221 2784 가로세로퍼즐

# 정답코드

words = [input() for _ in range(6)]
results = []
puzzle = []

for perm in permutations(words, 3):
    check = [False for _ in range(6)]

    vertical1 = perm[0][0] + perm[1][0] + perm[2][0]
    vertical2 = perm[0][1] + perm[1][1] + perm[2][1]
    vertical3 = perm[0][2] + perm[1][2] + perm[2][2]

    copy = words[:]

    for word in perm:
        copy.remove(word)

    for word in (vertical1, vertical2, vertical3):
        if word in copy:
            copy.remove(word)
            
    if not copy:        
        results.append(perm)

if results:
    for word in sorted(results)[0]:
        print(word)
else:
    print(0)




