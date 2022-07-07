def add(a, b):
    c = a + b
    return c


x = add(3, 2)
print(x)




def calc(a, b):
    c = a + b
    d = a - b
    return c, d  #tuple로서 여러 개의 값 리턴 가능. 3개 이상도 ㅎㅎ


print(calc(3, 2))



def is_prime(n):
    for denom in range(2, n):
        if n % denom == 0:
            return False     #return은 함수를 종료하시오. 더 이상 iterate 안함.
            #약수 2에서 바로 걸리면 False를 리턴하고 종료함. 함수 종료니 아래 True까지 갈 일이 없음
            #7이면 for문이 6까지 돌고 끝남.. return false 안함.. 즉 함수가 종료되지 않음.
    return True # 그렇지 않으면 True를 뱉으시오.


a = [7, 12, 13, 15]

for num in a:
    if is_prime(num):
        print(num, end=' ')

print()




def plus_one(x):
    return x+1


#lambda는 변수에 할당해서 사용 가능
plus_two = lambda x: x+2   # 표현식 내에서 사용하라네 파이썬이..
print(plus_two(3))


a=[1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))
#map(함수명, 자료)

#람다는 간단한 경우에만! 걍 한줄 식에서 편리하게 쓰자.