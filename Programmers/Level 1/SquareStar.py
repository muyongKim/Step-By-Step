# 직사각형 별찍기 21/01/31

n,m = map(int,input().strip().split(' '))

def solution(n,m):
    for i in range(0,m):
        print('*'*n)

solution(n,m)