# 220814 18870 좌표 압축

# 입력값 받기
N = int(input())
coordinate = list(map(int, input().split()))

# 중복값을 제거하고 정렬해준다.
no_same = list(set(coordinate))
no_same.sort()

# 압축된 좌표를 담을 딕셔너리
compress = {}
# 압축된 좌표를 key로, 원래 좌표를 value로 하는 딕셔너리를 만든다.
for i in range(len(no_same)):
    compress[no_same[i]] = i

# 양식에 맞게 압축된 좌표를 출력해준다.
for i in coordinate:
    print(compress[i], end=' ')