arr = input().upper()
result = [0 for _ in range(100)]
for val in arr:
    # print(ord(val))
    result[ord(val)] += 1
maximum = max(result)
max_idx = 0
cnt = 0
for i in range(len(result)):
    if result[i] == maximum:
        cnt += 1
        max_idx = i
if cnt >= 2:
    print('?')
else:
    # print(max`
    print(chr(max_idx))