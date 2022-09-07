# 220904 1541 잃어버린 괄호

# 정답코드

import sys
input = sys.stdin.readline

formula = list(input().strip())

stack = []
operator = []
temp = str()
for i in formula:
    if i.isdigit():
        temp += i
    else:
        stack.append(int(temp))
        temp = str()
        operator.append(i)
stack.append(int(temp))


ans = 0
while operator:
    op = operator.pop()
    if op == '+':
        num_1 = stack.pop()
        num_2 = stack.pop()
        stack.append(num_1 + num_2)
    else:
        ans -= stack.pop()

for number in stack:
    ans += number

print(ans)