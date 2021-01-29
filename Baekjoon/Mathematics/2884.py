# 알람 시계 2021/01/23

h, m = map(int, input().split())

if m - 45 < 0:
    h -= 1
    if h<0:
        h = 23
    m += 15
    print("%d %d" %(h,m))
else: 
    m -= 45
    print("%d %d" %(h,m))