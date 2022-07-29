# n이랑 m은 input만 받고 활용 안 한다.
n = int(input())
# input 받은 숫자들을 map을 통해서 리스트에 담는다.
temp1 = list(map(int, input().split()))
# 숫자들을 곱을 num1에 할당해준다.
num1 = 1
for i in temp1:
    num1 *=i

# 위와 동일
m = int(input())
temp2 = list(map(int, input().split()))
num2 = 1
for j in temp2:
    num2 *=j
    
# 유클리드 호제법을 통해 최대공약수를 구하는 함수를 정의한다.
def euclid_gcd(a, b): # a > b
    res = 0
    while b:
        res = a % b
        a = b
        b = res
    return a

result = euclid_gcd(num1, num2)
# 9자리 이하일 때는 그냥 출력한다.
if len(str(result)) <= 9:
    print(result)
# 10자리 이상일 때는 슬라이싱을 통해 뒤에 9자리만 출력한다.
else:
    print(str(result)[-9:len(str(result))])
    
