from bisect import bisect_left
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221002 1517 버블소트

# 정답코드


def merge_sort(arr):
    global cnt

    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []

    l, h = 0, 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] <= high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
            cnt += len(low_arr) - l

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr  


N = int(input())

numbers = list(map(int, input().split()))

cnt = 0

merge_sort(numbers)

print(cnt)