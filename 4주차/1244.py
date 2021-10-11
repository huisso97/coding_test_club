import sys
sys.stdin = open('1244.txt')

N = int(input())
switch = [0]+list(map(int, input().split()))
num = int(input())
student = []
for i in range(num):
    student.append(list(map(int, input().split())))

for i in range(num):
    if student[i][0] == 1:
        check = student[i][1]
        n = 1
        while 0<=check<=len(switch):
            check = check*n
            if check > len(switch):
                break
            if switch[check] == 1:
                switch[check] = 0
            else:
                switch[check] = 1
            n += 1
    if student[i][0] == 2:
        check = student[i][1]
        if switch[check] == 1:
            switch[check] = 0
        else:
            switch[check] = 1
        i = 1
        while 0<=check-i<=len(switch) and 0<=check+i<=len(switch):

            if switch[check-i] == switch[check+i]:
                if switch[check-i] == 0:
                    switch[check-i] = 1
                    switch[check+i] = 1
                else:
                    switch[check-i] = 0
                    switch[check+i] = 0
            i += 1
switch.pop(0)
while True:
    if len(switch) > 20:
        print(*switch[:20])
        del switch[:20]
    else:
        print(*switch)
        break
