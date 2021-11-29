arr = input().upper()
maximum = 0
result = [0 for _ in range(1, 100)]
for i in range(len(arr)):
    # print(ord(arr[i]))
    # print(ord[arr[i]])
    # print(result[ord[arr[i]]])
    result[ord(arr[i])] += 1
    # print(ord('A'))
    # print(ord('Z'))
    # print(chr(ord('Z')))
maximum = max(result)
max_idx = 0
cnt = 0
for i in range(len(result)):
    if result[i] == maximum:
        cnt += 1
        max_idx = i
        # print(max_idx)

if cnt >= 2:
    print('?')
else:
    print(chr(max_idx))