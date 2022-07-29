a = "AbaAeCe"
b = "baeeACA"

str1 = [0] * 52  # 대소문자 각 26개. 리스트에 0~51의 인덱스를 가져보자.
str2 = [0] * 52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1  # capital 65~90   #lower 97~122 -> 26
    else:
        str1[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1  # capital 65~90   #lower 97~122 -> 26
    else:
        str2[ord(x) - 71] += 1

# if str1 == str2: 이래도 됨. 근데 cpp 방식으로 하자면
for i in range(52):
    if str1[i] !=str2[i]:
        print("NO")
        break

else:
    print("YES")

