import sys
sys.stdin = open('1316.txt')

T = int(input())


for tc in range(T):
    words = input()
    sum = 0
    for i in range(len(words)):
        cnt = 0
        sub = words[i]
        if len(words) == 1:
            cnt = 1
        else:
            j = i+1
            while j < len(words):
                #다음 알파벳이랑 같으면
                if sub == words[j]:
                   cnt = 1

                #다음 알파벳이랑 같지 않을 때
                else:
                    #만약 해당 알파벳부터 끝까지 중에서 다시 나오면 cnt = 0
                    for k in range(j, len(words)):
                        if words[k] == sub:
                            cnt = 0
                            sum = cnt
                            break
                        else:
                            cnt = 1
                j += 1
        sum += cnt
print(sum)