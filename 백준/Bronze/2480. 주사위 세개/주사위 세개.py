num1, num2, num3 = map(int, input().split())

if num1 == num2 == num3:
    print(10_000 + num1 * 1_000)
elif num1 == num2:
    print(1_000 + num1 * 100)
elif num1 == num3:
    print(1_000 + num1 * 100) 
elif num2 == num3:
    print(1_000 + num2 * 100)
else:
    print(100 * max(num1, num2, num3))