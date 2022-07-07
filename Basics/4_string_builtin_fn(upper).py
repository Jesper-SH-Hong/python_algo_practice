msg ="It is Time"

print(msg.upper())
print(msg.lower())
print(msg)
tmp =msg.upper()
print(tmp)



print(tmp[0])  #String도 array. 인덱스 있음.
print(tmp.find('T')) #최초 대문자 T의 index 자리 뱉음.
print(tmp.count('T')) #해당 문자열이 how many

print(msg[:2]) #range처럼 뒤에껀 불포함
print(msg[0:2])

print(len(msg))  # whitespace 포함


for i in range(len(msg)):
    print(msg[i], end=' ')

print()

for x in msg:
    print(x, end='')
print()

for x in msg:
    if x.isupper():  #.islower()
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():
        print(x, end='')
print()

tmp = 'A'
for x in tmp:
    print(ord(x))   #ASCII #  A:65  Z:90
    print(chr(65))