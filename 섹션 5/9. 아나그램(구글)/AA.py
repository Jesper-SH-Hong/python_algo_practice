a = "AbaAeCe"
b = "baeeACA"


#[풀이2]
sH = dict()   #string hash
for x in a:
    sH[x] = sH[x] = sH.get(x,0) + 1
for x in b:
    sH[x] = sH[x] = sH.get(x,0) - 1

for x in a:
    if sH.get(x) > 0:  #잉 다 못 지웠냐?
        print("NO")
        break
else:
    print('yes')



#[풀이1]
# str1 = dict()
# str2 = dict()
#
# for x in a:
#     str1[x] = str1.get(x, 0) + 1  #str1 안에 x란 키가 없으면 디폴트인 0을 리턴, 거기에 +1, 있으면 그 키의 밸류를 리턴.  거기다 +1 누적하자 ㅋㅋ
#
# print(str1)
#
# for x in b:
#     str2[x] = str2.get(x,0) + 1

# for i in str1.keys():
#     if i in str2.keys():
#         if str1[i] != str2[i]:
#             print("NO")
#             break  #for문의 브레이크
#
#     else:
#         print("No")
#         break
# else:
#     print("Yes")




#[내 풀이]

# d = dict()
#
# for x in a:
#     d[x] = 0
#
# for x in a:
#     d[x] += 1
#
# for y in b:
#     d[y] -= 1
#
# if any(x !=0 for x in d.values()):
#     print("False")
# else:
#     print("true")
#
# print(d)
