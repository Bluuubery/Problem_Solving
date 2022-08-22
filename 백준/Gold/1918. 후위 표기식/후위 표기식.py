# 220822
# 연습문제1- extra

# 정답코드

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


# infix: 중위표기식, postfix: 후위표기식으로 변환한 식
infix = list(input())
postfix = str()
# stack: 연산자를 담을 스택
stack = []
for i in infix:
    # 숫자면 바로 후위표기식에 더해준다.
    if i.isalpha():
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
print(postfix)