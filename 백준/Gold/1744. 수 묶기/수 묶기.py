# 220906 1744 수 묶기

# 정답 코드

N = int(input())

positive = []
negative = []

for _ in range(N):
    number = int(input())
    if number > 0:
        positive.append(number)
    else:
        negative.append(number)

positive.sort(reverse=True)
negative.sort()

positive_sum = 0

if len(positive) % 2:
    for i in range(0, len(positive) - 2, 2):
        if positive[i] == 1 or positive[i + 1] == 1:
            positive_sum += positive[i] + positive[i + 1]
        else:
            positive_sum += positive[i] * positive[i + 1]
    positive_sum += positive[-1]

else:
    for i in range(0, len(positive) - 1, 2):
        if positive[i] == 1 or positive[i + 1] == 1:
            positive_sum += positive[i] + positive[i + 1]
        else:
            positive_sum += positive[i] * positive[i + 1]

negative_sum = 0

if len(negative) % 2:
    for i in range(0, len(negative) -2, 2):
        negative_sum += negative[i] * negative[i + 1]
    negative_sum += negative[-1]

else:
    for i in range(0, len(negative) - 1, 2):
        negative_sum += negative[i] * negative[i + 1]

print(positive_sum + negative_sum)