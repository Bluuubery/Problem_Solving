N = int(input())
N_list = []

while N:
    N_list.append(N)
    N = int(input())
else:
    pass

max_value = max(N_list)
num_list = [True] * (2*max_value + 1)

for i in range(2, int((2*max_value)** + 1)):
    if num_list[i] == True:
        j = 2
        while i*j <= 2*max_value:
            num_list[i*j] = False
            j += 1


for number in N_list:
    cnt = 0
    for i in range(number+1, 2*number+1):
        if i == 1:
            pass
        elif i == 2:
            cnt += 1
        else:
            if num_list[i] == True:
                cnt += 1
    print(cnt)