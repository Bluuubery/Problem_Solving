import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220928 10775 공항

# 정답코드

def find_gate(x):
    if gates[x] != x:
        gates[x] = find_gate(gates[x])
    return gates[x]



def docking(x, y):
    x = find_gate(x)
    y = find_gate(y)
    gates[x] = y
    
    return


def solve():
    ans = 0

    for _ in range(P):
        g = int(input())
        gate = find_gate(g)

        if gate == 0:
            print(ans)
            return
            
        docking(gate, gate - 1)
        ans += 1

    print(ans)
    return

gates = list(range(int(input()) + 1))
P = int(input())

solve()
