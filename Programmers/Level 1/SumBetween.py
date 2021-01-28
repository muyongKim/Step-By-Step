# 두 정수 사이의 합
# Input
a = 3
b = 5

def solution(a,b):
    answer = 0
    if a>b:
        for n in range(b,a+1):
            answer += n
    elif a<b:
        for n in range(a,b+1):
            answer += n
    else:
        answer = a
    return answer

print(solution(a,b))