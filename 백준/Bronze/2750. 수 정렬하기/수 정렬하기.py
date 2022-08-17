# 버블 정렬
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 선택 정렬
def selection_sort(arr):
    for i in range(len(arr) -1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 삽입 정렬
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

# 퀵정렬
def quick_sort(arr, start, end):
    if start >= end:
        return
    pv = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and arr[left] <= arr[pv]:
            left += 1

        while right > start and arr[right] >= arr[pv]:
            right -= 1

        if left > right:
            arr[right], arr[pv] = arr[pv], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

# 병합 정렬
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []

    l, h = 0, 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

# 카운트 정렬
def count_sort(arr):
    def maxv(b):
        max = b[0]
        for i in b:
            if i > max:
                max = i
        return max

    temp = [0] * (maxv(arr) + 1)
    temp2 = [0] * len(arr)

    for i in arr:
        temp[i] += 1

    for i in range(1, len(temp)):
        temp[i] += temp[i - 1]

    for i in range(len(temp2)-1, -1, -1):
        temp[arr[i]] -= 1
        temp2[temp[arr[i]]] = arr[i]
    return temp2

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))
    
for number in merge_sort(numbers):
    print(number)