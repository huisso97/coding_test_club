import sys
sys.stdin = open('13300.txt')

N, K = map(int, (input().split()))
student = []
for i in range(N):
    student.append(list(map(int, input().split())))
student.sort()
# print(student)
room = 1
i = 0
tmp = [student[0]]
for i in range(1, len(student)):
    if student[i] == tmp[-1]:
        if len(tmp) < K:
            tmp.append(student[i])
        else:
            room += 1
            tmp = [student[i]]
    else:
        room += 1
        tmp = [student[i]]
print(room)
