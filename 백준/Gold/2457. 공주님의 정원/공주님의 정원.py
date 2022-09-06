# 220906 2457 공주님의 정원

# 정답코드
import sys
input = sys.stdin.readline


def month_to_day(month, day):
    month_dict = {
        1: 0,
        2: 31,
        3: 59,
        4: 90,
        5: 120,
        6: 151,
        7: 181,
        8: 212,
        9: 243,
        10: 273,
        11: 304,
        12: 334,
    }
    return month_dict[month] + day


# def find_next_flower(end):
#     global flower
#     flower.sort(key=lambda x:x[1], reverse=True)

#     for i in range(N):
#         if flower[i][0] <= end:
#             if flower[i][1] > end:
#                 end = flower[i][1]
#                 flower.remove(flower[i])
#                 return end
#     else: 
#         return 0

N = int(input())

flower = []
for _ in range(N):
    month_start, day_start, month_end, day_end = map(int, input().split())
    start = month_to_day(month_start, day_start)
    end = month_to_day(month_end, day_end)
    flower.append((start, end))

flower.sort(key=lambda x:x[1], reverse=True)

end = 60
cnt  = 0

flag = True

while end <= 334 and flag:
    for times in flower:
        if times[0] <= end:
            if times[1] > end:
                end = times[1]
                cnt += 1
                flower.remove(times)
                break
    else:
        flag = False
        break

if end <= 334:
    cnt = 0
    
print(cnt)