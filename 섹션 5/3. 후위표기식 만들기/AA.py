a = "3+5*2/(7-2)"
stack = []
res = ""

for x in a:
    if x.isdecimal():  # 십진수인가
        res += x
    else:

        if x == "(":
            stack.append(x)

        elif x == "*" or x == "/":
            while stack and (stack[-1] == '*' or stack[-1] == '/'):  # stack의 최상단 자료
                res += stack.pop()
            stack.append(x)

        elif x == '+' or x == '-':
            while stack and stack[-1] != "(":  # 죽죽 끄집어내라 ㅋㅋㅋ 아 괄호 속 연산인 경우엔 pop 하다가 ( 걸리기 전까지만 뽑아내기..
                res += stack.pop()  # 괄호 사이 연산자만 처리
            stack.append(x)

        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()  # 괄호 처리중이니 괄호 시작도 제거해야해서 아랫줄.
            stack.pop()       #다 돌았으면 괄호 제거해주세용.

while stack:  # 그러고도 stack에 남아있냐
    res += stack.pop()

print(res)
