s = "()(((()())(())()))(())"
sum = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == '(':  # 바로 앞이 (니까    () 레이저군
            # stack.pop()
            sum += len(stack)    # 레이저 앞에 ( 들은 다 조각날 쇠막대기의 개수일테니(그림 그려보셈)

        else:    #쇠막대의 마지막 조각이구나 걍 1조각 추가해주면 되겠네
            # stack.pop()
            sum += 1




# print(stack)
print(sum)
