import sys
sys.stdin = open('input.txt')

# arr = list(input())
# # print(arr)
# num_list = list(i for i in range(10))
# cnt = 1
# for i in range(len(arr)):
#     num = int(arr[i])
#     if num in num_list:
#         num_list.remove(num)
#     else:
#         if num == 6 and 9 in num_list:
#             num_list.remove(9)
#         elif num == 9 and 6 in num_list:
#             num_list.remove(6)
#         else:
#             # print/(num_list)
#             num_list = list(i for i in range(10))
#             num_list.remove(num)
#             cnt += 1
# 9 -> 6
# 해당 숫자를 인덱스로 아하~~
# 9를 6으로 아하~~~
# 이해했어!
# 응응
# 알겠어ㅓㅇ어엉
# print(cnt)
arr = list(input())
tmp = [0]*9

# print(tmp)
cnt = 1
for i in range(len(arr)):
    # print(tmp)
    # print(cnt)
    if arr[i] == '9':
        arr[i] = '6'
    num = int(arr[i])
    # if tmp[num] == 0:
    tmp[num] += 1
if tmp[6] % 2:
    tmp[6] = tmp[6]//2+1
else:
    tmp[6] = tmp[6] // 2
maximum = max(tmp)
print(maximum)
