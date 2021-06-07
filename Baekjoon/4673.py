# 셀프 넘버 2021/06/07
# 분류 : 수학, 구현

def d(n):
    for v in str(n):
        n += int(v)    
    return n

num = []
n = 1
while n <= 10000:
    num.append(d(n))
    n += 1

for i in range(1,10001):
    if i not in num:
        print(i)