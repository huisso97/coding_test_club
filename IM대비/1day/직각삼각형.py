while True:
    lines = list(map(int, input().split()))
    if sum(lines) ==0:
        break
    else:
        max_list = max(lines)
        lines.remove(max_list)
        if lines[0]**2 + lines[1]**2 == max_list**2 :
            print('right')
        else:
            print('wrong')