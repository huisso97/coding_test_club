import sys
sys.stdin = open('1251.txt')

word= list(input())

tmp = []
for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        a = word[:i+1]
        b = word[i+1:j+1]
        c = word[j+1:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a+b+c)
tmp.sort()
print(''.join(tmp[0]))

word= list(input())

# T = int(input())
#
# for tc in range(1, T+1):
#     word = input()
#     n = len(word)
#     answer = []
#     tmp = []
#
#     for i in range(1, n-1):
#         for j in range(i+1, n):
#             a = word[:i][::-1]
#             b = word[i:j][::-1]
#             c = word[j:][::-1]
#             tmp.append(a+b+c)
#
#     for word in tmp:
#         answer.append(''.join(word))
#
#     print(sorted(answer)[0])
#     #
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 tmp = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
#                 answer.append(tmp)
#     print(min(answer))