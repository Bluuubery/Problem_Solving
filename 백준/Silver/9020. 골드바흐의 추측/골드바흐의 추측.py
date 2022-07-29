import math

n = int(input())

prime = [0, 0] + ([1] * (10000))
for i in range(2, int(math.sqrt(10000) + 1)):
    if prime[i]:
        for j in range(i * 2, len(prime), i):
            prime[j] = 0

for _ in range(n):
    even_num = int(input())
    a = even_num//2
    b = a
    while True:
        if prime[a] and prime[b]:
            print(a, b)
            break
        else:
            a += -1
            b += +1