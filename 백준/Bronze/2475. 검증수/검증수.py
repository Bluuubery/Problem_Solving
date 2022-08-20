# 220821 2475 검증수

import sys

input = sys.stdin.readline

serial_num = list(map(int, input().split()))
verification_num = sum(map(lambda x : x**2, serial_num)) % 10

print(verification_num)