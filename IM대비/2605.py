#start를 기준으로 나열하기
#0이면 start 뒤
#1이면 start 앞
#2이면 start보다 앞앞
#이거를 어케 구현함..
n = int(input())
ls = [map(int, input().split())]
students = []

for i in range(n):
    students[i] = ls[i]
print(students)