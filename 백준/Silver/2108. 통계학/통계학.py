import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

if len(nums) == 1:
    mode = nums[0]
else:
    temp = Counter(nums).most_common()
    if temp[0][1] == temp[1][1]:
        mode = temp[1][0]
    else:
        mode = temp[0][0]


# print(temp)
#
# if len(nums) == 1:
#     mode = nums[0]
# else:
#     temp = {}
#     for i in nums:
#         temp[i] = nums.count(i)
#
#     temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
#     if temp[0][1] == temp[1][1]:
#         mode = temp[1][0]
#     else:
#         mode = temp[0][0]


average = round(sum(nums) / len(nums))
mean = nums[len(nums)//2]
num_range = nums[-1] - nums[0]

print(average)
print(mean)
print(mode)
print(num_range)