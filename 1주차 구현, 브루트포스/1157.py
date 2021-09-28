words = list(input().upper())

words_list = list(set(words))

# print(words, words_list)
# ['M', 'I', 'S', 'S', 'I', 'S', 'S', 'I', 'P', 'I'] {'S', 'M', 'I', 'P'}

result = []
for i in range(len(words_list)):
    cnt = 0
    for j in range(len(words)):
        if words_list[i] == words[j]:
            cnt += 1
    result.append(cnt)

maximum = [0, 0]
for k in range(len(result)):
    if result[k] > maximum[1]:
        maximum = [k, result[k]]
    #가장 많이 사용된 알파벳이 여러개 일 경우
    elif result[k] == maximum[1]:
        print('?')
        break
else:
    print(words_list[maximum[0]])