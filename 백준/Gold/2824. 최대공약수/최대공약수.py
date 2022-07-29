n = int(input())
temp1 = list(map(int, input().split()))
num1 = 1
for i in temp1:
    num1 *=i

m = int(input())
temp2 = list(map(int, input().split()))
num2 = 1
for j in temp2:
    num2 *=j

def euclid_gcd(a, b): # a > b
    res = 0
    while b:
        res = a % b
        a = b
        b = res
    return a

result = euclid_gcd(num1, num2)
# print(result)
if len(str(result)) <= 9:
    print(result)
else:
    print(str(result)[-9:len(str(result))])
    