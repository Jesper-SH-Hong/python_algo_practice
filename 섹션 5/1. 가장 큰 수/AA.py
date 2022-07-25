# 내 바로 앞에 나보다 작은 수가 있으면 그 놈을 지우고.. 내가 젤 앞자리 수로..
# 작지 않으면(같을 수도..) 살려두고 들가자.

# 8 입장에선 더 지울 수가 없으니 7은 살려둔다..


# 이렇게 지우고 밀고 쉽게할 수 있는 자료구조가 Stack임.

# Last in First Out. 나중에 들어간 게 먼저 나옴.

# 운동장에 파인 구덩이라 생각. 축구공들 뺴려면 최근에 박힌 놈부터 뺴야함.
# 골목 주차. 출구가 하나라고 생각하셈

# 파이썬에는 stack 자료구조가 없어서 걍 append와 pop으로 구현됨.

num = 5276823
num = list(map(int, str(num)))  # str만 각 자리수가 idx로 접근 가능
m = 3

stack = []
prev = 0

for x in num:
    while m > 0 and stack and stack[-1] < x:  # 일단 내 앞자리에 나보다 작은 놈은 다 제거
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-2]

res = ''.join(map(str, stack))  # 뭐 이런 것도 있따.. for문으로도 가능

print(stack)
print(res)
