import math
n, s = map(int, input().split())
sisters = list(map(int, input().split()))
distance = [abs(i - s) for i in sisters]
print(math.gcd(*distance))
