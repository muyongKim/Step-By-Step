# 다음 큰 숫자 2021/02/21
# Input
n = 78

def solution(n):
    n = format(n,'b')
    n_cnt = 0
    
    for i in n:
        if i == '1':
            n_cnt += 1

    while True:
        cnt = 0
        n = int(n, 2)
        n += 1
        n = format(n,'b')

        for i in n:
            if i == '1':
                cnt += 1
        if cnt == n_cnt:
            break
    
    n = int(n,2)

    return n 

print(solution(n))