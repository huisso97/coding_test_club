receive = 1000 - int(input())

count = 0
ls = [500, 100, 50, 10, 1]
for i in ls:
    count += receive // i 
    receive = receive % i
print(count)