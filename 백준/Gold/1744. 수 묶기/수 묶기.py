# 220906 1744 수 묶기

# 정답 코드

import sys
input = sys.stdin.readline


# N: 수열의 크기
N = int(input())

# 수열을 정렬 후 양수, 음수로 나누어서 양 끝에서부터 괄호로 묶는다.

# positive: 양수만 담은 수열, negative: 음수와 0만 담은 수열
positive = []
negative = []
for _ in range(N):
    number = int(input())
    if number > 0:
        positive.append(number)
    else:
        negative.append(number)

# 두 수열을 정렬한다.(양끝에서 접근하므로 양수 수열은 역순으로 정렬)
positive.sort(reverse=True)
negative.sort()

# positive_sum: 양수 수열의 최대합
positive_sum = 0
# 양수 수열이 홀수일 경우
if len(positive) % 2:
    # 두 개씩 묶어서 곱해서 더해주고 짝이 없는 마지막 수는 따로 더해준다.
    for i in range(0, len(positive) - 2, 2):
        # 1일 경우 곱하지 않고 더해준다.
        if positive[i] == 1 or positive[i + 1] == 1:
            positive_sum += positive[i] + positive[i + 1]
        else:
            positive_sum += positive[i] * positive[i + 1]
    positive_sum += positive[-1]
# 짝수일 경우
else:
    # 두 개씩 묶어서 곱해서 더해준다.
    for i in range(0, len(positive) - 1, 2):
        # 1일 경우 곱하지 않고 더해준다.
        if positive[i] == 1 or positive[i + 1] == 1:
            positive_sum += positive[i] + positive[i + 1]
        else:
            positive_sum += positive[i] * positive[i + 1]

# negative_sum: 음수 수열의 최대합
negative_sum = 0
# 음수 수열이 홀수일 경우
if len(negative) % 2:
    # 두 개씩 묶어서 곱해서 더해주고 짝이 없는 마지막 수는 따로 더해준다.
    for i in range(0, len(negative) -2, 2):
        negative_sum += negative[i] * negative[i + 1]
    negative_sum += negative[-1]
# 짝수일 경우
else:
    # 두 개씩 묶어서 곱해서 더해준다.
    for i in range(0, len(negative) - 1, 2):
        negative_sum += negative[i] * negative[i + 1]

# 수열 전체의 최대합 출력
print(positive_sum + negative_sum)