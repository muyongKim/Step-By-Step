# 더하기 사이클 2021/01/24

N = input()
first = N
cycle = 0

if int(N)<10:
    N = '0'+N

while True:
    tmp = str(int(N[0])+int(N[1]))

    if int(tmp)>=10:
        tmp = str(tmp[1])
    N = N[1]+tmp
    cycle += 1

    if int(N) == int(first):
        break

print(cycle)