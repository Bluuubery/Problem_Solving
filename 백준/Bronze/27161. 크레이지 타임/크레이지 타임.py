# 230114 C: 크레이지 타임

N = int(input())
time = 0
reverse = 1

for _ in range(N):
    # 동작
    action = 'NO'

    # 입력
    card_type, card_time = input().split()
    card_time = int(card_time)

    # 시간 계산
    if reverse == -1:
        if time == 1:
            time = 12
        else:
            time -= 1
    else:
        if time == 12:
            time = 1
        else:
            time += 1

    # 모래 시계
    if card_type == 'HOURGLASS':
        # 과부화
        if time == card_time:
            pass
        
        # 역전
        else:
            reverse *= -1

    # 동기화
    else:
        if time == card_time:
            action = 'YES'

    # print(time, card_type, card_time, reverse)
    print(time, action)
    # print()

