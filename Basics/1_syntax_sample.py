a, b = input("a, b에 넣을 숫자를 입력하세요: ").split()
#사용자가 2, 3 치면 각 변수에 저장됨

print(a, b)
print(a + b)
c = a + b     #str.   '2' + '3' = '23'

print(type(a))
print(type(c))

a, b = map(int, input("Enter nums: ").split())
print(type(a))
print(a + b)   #int. 5
print(a//b)  #몫
print(a%b) #remainder
print(a**b) #b승
