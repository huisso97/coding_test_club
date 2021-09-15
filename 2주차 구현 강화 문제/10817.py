A,B,C = map(int, input().split())

if A >= B and A >= C:
    if B >= C:
        print(B)
    elif C >= B:
        print(C)
elif B >= A and B >= C:
    if A >= C:
        print(A)
    elif C >= A:
        print(C)
elif C >= A and C >= B:
    if B >= A:
        print(B)
    elif A >= B:
        print(A)