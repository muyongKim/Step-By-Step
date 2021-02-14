# 콜라츠 추측 2021/02/14
# Input
num = 626331

def solution(num):
    cnt = 0
    while not num == 1:
        if num%2 == 0:
            num /= 2
        else:
            num = num*3 + 1
        cnt += 1

        if cnt == 500:
            return -1

    return cnt

print(solution(num))