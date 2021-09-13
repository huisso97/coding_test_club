import sys
sys.stdin = open('2605.txt')

#그리디였다 규칙을 찾아보자~!
n = int(input())
numbers = list(map(int, input().split()))

result = []

for idx in range(len(numbers)):
    #idx+1 = 해당 값 들어왔을때의 리스트 길이
    #location = 해당 인덱스가 서있을 위치
    location = (idx+1)-1-numbers[idx]
    result.insert(location, idx+1)
print(*result)














# #학생 나열
# ordered_st = []
# #번호 나열
# ordered_num = []
# idx = 1
# for i in range(n):
#     #첫번째는 일단 넣고
#     if numbers[i] == 0:
#         ordered_st.append(numbers.index(i))
#         ordered_num.append(numbers[i])
#     #두번째부터
#     else:
#         #앞의 번호보다 크면
#         if numbers[i] > ordered_num[-1]:
#             ordered_st.append(numbers.index(i))
#         #앞의 번호랑 같다 == 앞의 번호보다 뒤에 선다
#         elif numbers[i] == ordered_num[-1]:
#             k = ordered_st.pop()
#             ordered_st.append(numbers.index(i))
#             ordered_st.append(k)
#         else:
