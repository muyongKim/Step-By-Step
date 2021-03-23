# n진수 게임 2021/03/23
# Input
n = 16
t = 16
m = 2
p = 2

def convert(number, base):
    nums = "0123456789ABCDEF"
    q, r = divmod(number, base)
    if q == 0:
        return nums[r]
    else:
        return convert(q, base) + nums[r]

def solution(n,t,m,p):
    answer = ""
    length = t * m
    cnt = 0
    num = []

    while len(num) < length:
        tmp = convert(cnt, n)
        for i in tmp:
            num.append(i)
            if len(num) == length:
                break
        cnt += 1
    
    # print(num)

    for i in range(len(num)):
        order = (i+1) % m
        if order == 0:
            order = m
        
        if order == p:
            answer += num[i]
    
    return answer
        

print(solution(n,t,m,p))