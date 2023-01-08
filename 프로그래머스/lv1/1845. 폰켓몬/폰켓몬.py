def solution(nums):
    N = len(nums)

    nums_set = set(nums)
    answer = min(N // 2, len(nums_set))
    return answer