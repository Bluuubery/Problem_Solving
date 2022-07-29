import math

n = int(input())

# 0부터 10000까지의 소수를 구한다.(에라토스테네스의 체 활용)
prime = [0, 0] + ([1] * (10000))
for i in range(2, int(math.sqrt(10000) + 1)):
    if prime[i]:
        for j in range(i * 2, len(prime), i):
            prime[j] = 0

# n에 대해 가운데(n/2)부터 양옆으로 펼쳐나가면서 두 수가 소수인지 검증한다.
for _ in range(n):
    even_num = int(input())
    a = even_num//2
    b = a
    while True:
        # 소수일 경우 두 숫자를 출력하고 중단한다.
        if prime[a] and prime[b]:
            print(a, b)
            break
        # 소수가 아닐 경우 각각 +1 / -1 해주고 다시 소수인지 검증한다.
        else:
            a += -1
            b += +1
