# 220814 18870 좌표 압축

N = int(input())

nums = list(map(int, input().split()))
nums_no_same = list(set(nums))
nums_no_same.sort()
nums_dict = {}

for i in range(len(nums_no_same)):
    nums_dict[nums_no_same[i]] = i


for i in nums:
    print(nums_dict[i], end=' ')