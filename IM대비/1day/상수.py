num1, num2 = input().split()
if int(num1[::-1]) > int(num2[::-1]) :
    print(num1[::-1])
else:
    print(num2[::-1])