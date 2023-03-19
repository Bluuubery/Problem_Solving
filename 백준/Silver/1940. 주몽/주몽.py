import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
left = 0
right = N - 1

while True:
    if left >= right:
        break
    
    if arr[left] + arr[right] == M:
        ans += 1
        left += 1
        right -= 1
        
    elif arr[left] + arr[right] < M:
        left += 1
    else:
        right -= 1
        
print(ans)