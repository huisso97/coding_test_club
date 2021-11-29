N, K = map(int, input().split())
student = []
for i in range(N):
    S, Y = map(int, input().split())
    student.append([S,Y])
student.sort()
room = 1
tmp = [student[0]]
for i in range(1, len(student)):
    #성별이 같아
    if student[i][0] == tmp[-1][0]:
        #학년이 같아
        if student[i][1] == tmp[-1][1]:
            if len(tmp) < K:
                tmp.append(student[i])
            elif len(tmp) == K:
                tmp = [student[i]]
                room += 1
        else:
            tmp = [student[i]]
            room += 1
    #성별이 달라
    else:
        tmp = [student[i]]
        room += 1

print(room)