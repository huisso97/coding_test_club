N, K = map(int, input().split())
tempartures = list(map(int, input().split()))

for i in range(0, len(tempartures)-K+1):
    maximum = sum(tempartures[:2])
    for j in range(i, len(tempartures)-K+1):
        if maximum < sum(tempartures[j:j+K+1]):
            maximum = sum(tempartures[j:j+K+1])
print(maximum)