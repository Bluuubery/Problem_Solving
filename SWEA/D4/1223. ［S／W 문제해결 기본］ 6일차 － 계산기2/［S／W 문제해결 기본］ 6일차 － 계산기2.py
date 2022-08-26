# 220822
# 1223 계산기

# 정답코드

# import sys
#
# sys.stdin = open('input.txt', 'r')


# 스택에 삽입할 때 우선순위 반환 함수
def in_coming_priority(op):
    if op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    elif op =='(':
        return 3


# 스택 내에 있을 때의 우선순위 반환 함수
def in_stack_priority(op):
    if op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    elif op =='(':
        return 0


def prefix(infix):
    postfix = str()
    # stack: 연산자를 담을 스택
    stack = []

    for i in infix:
        # 숫자면 바로 후위표기식에 더해준다.
        if i.isdigit():
            postfix += i
            continue
        # 닫는 괄호일 경우 여는 괄호가 나올 떄까지 스택을 비우고 후위 표기식에 더해준다.
        elif i == ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    postfix += stack.pop()
        # 그 외 연산자(괄호x)
        else:
            while True:
                # 스택이 비어있지 않고 스택 최상단 원소보다 우선순위가 낮을 경우 스택을 비우고 후위식에 더해준다.
                if stack and in_coming_priority(i) <= in_stack_priority(stack[-1]):
                    postfix += stack.pop()
                # 스택이 비어있거나 우선순위가 높을 경우 스택에 넣어준다.
                else:
                    stack.append(i)
                    break

    # 계산식 전체 검증 후 스택이 남아있으면 스택을 비우고 후위표기식에 더해준다.
    while stack:
        postfix += stack.pop()

    return postfix


# 연산자 변환 함수 선언
def my_op(num1, num2, op):
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    return ops[op](num1, num2)


for t in range(1, 11):
    N = int(input())
    infix = input()

    stack = []
    for i in prefix(infix):
        # 숫자면 스택에 넣어준다.
        if i.isdigit():
            stack.append(i)
        # 연산자면 스택에서 필요한 만큼 숫자를 빼내서 연산을 수행 후 다시 스택에 넣어준다.
        else:
            x = int(stack.pop())
            y = int(stack.pop())
            stack.append(my_op(x, y, i))
    
    # 최종 연산 결과를 스택에서 빼내서 출력한다.
    print('#{} {}'.format(t, stack.pop()))

