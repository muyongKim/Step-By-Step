# 하샤드 수 2021/02/14
# Input
x = 11

def solution(x):
    x = str(x)
    sum = 0
    for i in x:
        sum += int(i)

    if int(x) % sum == 0:
        return True
    else:
        return False

print(solution(x))