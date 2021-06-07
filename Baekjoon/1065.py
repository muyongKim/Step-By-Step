# 한수 2021/06/07
# 분류 : brute force

n = int(input())
if n <= 99:
    print(n)
else:
    cnt = 0
    i = '100'
    while int(i) <= n:
        d = int(i[1]) - int(i[0])
        for j in range(1,len(i)):
            if j == len(i) - 1:
                cnt += 1
                break
            else:
                if d != int(i[j+1]) - int(i[j]):
                    break
        i = str(int(i)+1)
    print(99+cnt)