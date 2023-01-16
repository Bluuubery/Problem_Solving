# 230116 2659 십자카드 문제


from collections import deque
from itertools import product 


numbers = list(map(str, input().split()))

def get_clock(numbers:list):
    numbers = deque(numbers)
    clock_num = int(''.join(numbers))
    for _ in range(4):
        numbers.rotate()
        clock_num = min(clock_num, int(''.join(numbers)))

    return clock_num

clock_num = get_clock(numbers)

clock_num_set = set()

ans = 0
for prod in product(['1', '2', '3', '4', '5', '6', '7', '8', '9'], repeat=4):
    clock_num_set.add(get_clock(list(prod)))

for num in clock_num_set:
    if clock_num >= num:
        ans += 1

print(ans) 
