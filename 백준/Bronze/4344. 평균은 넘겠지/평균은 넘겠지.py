n =int(input())

for i in range(n):
    score = list(map(int, input().split()))
    avg_score = sum(score[1:]) / score[0]
    cnt = 0

    for i in score[1:]:
        if i > avg_score:
            cnt += 1

    rate = cnt / score[0] * 100
    print(f'{rate:.3f}%')
    