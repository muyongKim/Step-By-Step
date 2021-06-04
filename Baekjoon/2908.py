# 상수 2021/06/04
# 분류 : 구현

A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)