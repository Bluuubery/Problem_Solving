a, b = input().split()

a_reverse = int(a[::-1])
b_reverse = int(b[::-1])

if a_reverse > b_reverse:
    print(a_reverse)
else:
    print(b_reverse)