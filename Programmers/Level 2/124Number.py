# 124 나라의 숫자 2021/03/02
# Input
n = 4

def solution(n):
    answer = ""
    num = "412"

    while n:
        n, mod = divmod(num, 3)
        answer = num[mod] + answer
        
        if not mod:
            n -= 1
    
    return answer