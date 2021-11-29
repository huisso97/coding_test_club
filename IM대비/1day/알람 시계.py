a, b = input().split(' ')
h = int(a)
m = int(b)
# h 시 m 분

if h == 0:
    total = 24*60 + m - 45
else:
    total = h*60 + m - 45

new_h = total // 60
new_m = total % 60

print(new_h, new_m)

# 틀렸다는디.. 