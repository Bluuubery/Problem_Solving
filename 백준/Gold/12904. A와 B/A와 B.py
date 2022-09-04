# 220904 12904 A와 B

# 정답코드

S = input()
T = input()

cnt = len(T) - len(S)
idx = 0
while True:
    idx += 1

    if T[-1] == 'A':
        T = T[0:-1]
    else:
        T = T[0:-1]
        T = T[::-1]
    
    if idx == cnt:
        break
    

if S == T:
    print(1)
else: 
    print(0)
