import sys
sys.stdin = open('1452.txt')

ulim = list(map(int, input().split()))
start = list(map(int, input().split()))
exist = False
ulism_sum = 0
start_sum = 0
for i in range(len(ulim)):
    ulism_sum += ulim[i]
    if ulism_sum > start_sum:
        exist = True
    start_sum += start[i]
if exist == True and sum(start) > sum(ulim):
    print('Yes')
else:
    print('No')
# for i in range(len(ulim)-1):
#     for j in range(i+1, len(ulim)):
#         # print(ulim[:j])
#         # print(start[:j])
#         if sum(ulim[:j]) > sum(start[:j]) and sum(ulim[j:]) < sum(start[j:]):
#             print('Yes')
#             exist = True
#             break
#     if exist:
#         break
#
#     else:
#         print('No')
#         break
