# 1924 2007년
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, d = map(int, input().split())

temp = (sum(month[:m-1]) + d) % 7 

print(day[temp])


