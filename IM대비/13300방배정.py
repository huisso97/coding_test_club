import sys
sys.stdin = open('13300.txt')
def Check(students, idx):
    girl = [0]*7
    boy = [0]*7
    while idx < len(students):
        if students[idx][0] == 0:
            girl[students[idx][1]] += 1
        else:
            boy[students[idx][1]] += 1
        idx += 1
    return girl, boy
def Room(student, K):
    global room
    for i in range(1,7):
        if student[i] > K:
            room += student[i] // K
            if student[i] % K:
                room += 1
        elif 0<student[i]<=K:
            room += 1
    return
N, K = map(int, input().split())
students = []
for i in range(N):
    students.append(list(map(int, input().split())))
room = 0
girl, boy = Check(students, 0)
Room(girl, K)
Room(boy, K)
print(room)