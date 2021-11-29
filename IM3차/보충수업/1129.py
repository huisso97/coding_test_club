# text = 'This iss a book~!'
# pt = 'iss'
# res = '없다'
#
# lt = 0
# rt = 0
# while True:
#     if pt[lt] == text[rt]:
#         if lt == len(pt)-1:
#             res = '있다'
#             break
#         lt += 1
#         rt += 1
#     else:
#         lt = 0
#         rt += 1

text = 'This iss a book~!'
pt = '~!'
res = '없다'
for i in range(len(text)-len(pt)+1):
    cnt = 0
    for j in range(len(pt)):
        if text[j+i]==pt[j]:
            cnt += 1
            continue
        else:
            break
    if cnt == len(pt):
        res = '있다'

print(res)