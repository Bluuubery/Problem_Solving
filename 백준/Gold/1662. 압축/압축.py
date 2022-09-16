# 220917 1662 압축

# 정답코드

string = input()

stack = []



for i in range(len(string)):



    if string[i] == '(':
        stack.append(string[i])
    


    elif string[i] == ')':

        length = 0

        while True:
            char = stack.pop()

            if char == '(':
                break

            length += char
        
        stack.append(stack.pop() * length)



    else:
        
        if i < len(string) - 1 and string[i + 1] == '(':
            stack.append(int(string[i]))

        else: 
            stack.append(1)


    # print(stack)



print(sum(stack))