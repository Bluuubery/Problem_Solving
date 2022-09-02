n = int(input())

for i in range(n):
    result = list(input())
    score = 0
    a = 0
    for i in result:
        if i == 'O':
            a += 1
            score += a
        if i == 'X':
            a = 0
    print(score)
