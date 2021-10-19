N = int(input())
meetings = []
for i in range(N):
    meetings.append(list(map(int, input().split())))
    meetings.sort(key=lambda x:(x[1], x[0]))
    # meetings.s/ort()
print(meetings)
cnt = 1
end_time = meetings[0][1]

for i in range(1, len(meetings)):
    if meetings[i][0]>=end_time:
        cnt += 1
        end_time = meetings[i][1]
print(cnt)
