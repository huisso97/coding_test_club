# 인덱스상으로 인덱스1이 2인격이므로, 0을 넣어서 만들어야함
# card = [i for i in range(1, 21)]
card = [i for i in range(21)]
# print(card)
for i in range(10):
    s, e = map(int, input().split())
    for j in range((e-s+1)//2):
        card[s+j], card[e-j] = card[e-j], card[s+j]
card.pop(0)
print(card)