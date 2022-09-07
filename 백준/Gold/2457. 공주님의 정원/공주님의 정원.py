# 220906 2457 공주님의 정원

# 정답코드
import sys
input = sys.stdin.readline


# month_to_day: 월과 일로 된 날짜로 일수로 바꿔주는 함수
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


# N: 꽃들의 총 개수
N = int(input())

# flower: 꽃들의 피고 지는 날짜를 담은 리스트
flower = []
for _ in range(N):
    month_start, day_start, month_end, day_end = map(int, input().split())
    start = month_to_day(month_start, day_start)
    end = month_to_day(month_end, day_end)
    flower.append((start, end))

# 지는 날짜 기준 내림차순으로 정렬해준다.
flower.sort(key=lambda x:x[1], reverse=True)

# 3월 1일: 60, 11월 30일: 334


# 처음 꽃만 찾으면 꽃이 지는 날짜만 고려해도 된다.
# end: 꽃이 지는 날짜(시작하는 꽃 찾기 위해 3월1일로 초기화)
# cnt: 선택한 꽃의 개수
end = 60
cnt  = 0

flag = True
# 11월30일 전까지 탐색
while end <= 334 and flag:
    # 현재 꽃이 지기 이전에 피는 꽃을 찾는다. 
    for times in flower:
        if times[0] <= end:
            # 선택한 꽃의 지는 날이 현재 꽃의 지는 날 이후
            if times[1] > end:
                # 꽃이 지는 날짜를 선택한 꽃으로 갱신해주고 꽃을 센다.
                end = times[1]
                cnt += 1
                # 탐색 중단
                break
    # 다음 꽃이 없으면 중단한다.
    else:
        flag = False
        break

# 11월 30일 이전에 꽃이 중단되면 0 출력
if end <= 334:
    cnt = 0
    
print(cnt)