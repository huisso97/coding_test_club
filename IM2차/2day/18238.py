# alpha = ['A',]
# print(ord('A'))
# print(ord('Z'))

alpha = []
for i in range(65, 91):
    alpha.append(chr(i))
# print(alpha)
length = len(alpha) // 2
# print(length)

string = input()

result = 0
start = 0
for i in range(len(string)):
    if alpha.index(string[i]) <= length:
        result +=alpha.index(string[i])
    else:
        #역행하면 1 더 빼줘야함 혹시나~~~ ㅎㅎ 0 
        result += abs(alpha.index(string[i]) - len(alpha) - 1)
print(result)

# 이거 어려워 ㅠㅠ 알겠습니다 도와주셔서 감사해요 재호아니 내가 언제 그 항상 우러러보죠 왜그러십니까
#으잉?! 내가 으 약아빠지긴 ~~~~ 아뉘,,,, ㅇㄴㄹㅇㄹㄴㄴㄴㅇㄹㅇ