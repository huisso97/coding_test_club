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

for i in range(len(string)):
    if alpha.index(string[i]) <= length:
        result +=alpha.index(string[i])
    else:
        #역행하면 1 더 빼줘야함 혹시나~~~ ㅎㅎ 
        result += abs(alpha.index(string[i]) - len(alpha) - 1)
print(result)