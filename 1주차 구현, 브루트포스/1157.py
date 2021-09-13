words = list(input().upper())

#리스트나 튜플형으로 알파벳의 개수와 알파벳을 묶어서 비교

#많이 쓰인 알파벳 수 비교값
maximum = 0
#많이 쓰인 알파벳 리스트
maximum_words = []
for i in range(len(words)):
    #알파벳 장 수
    sub = 0
    for j in range(i+1, len(words)):
        if words[i] == words[j]:
           sub += 1
        if sub > maximum:
            maximum_words.append(words[i])
if len(maximum_words)>1:
    print('?')
else:
    print(maximum_words[0])