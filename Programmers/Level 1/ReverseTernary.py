# 3진법 뒤집기
# Input
n = 125

def solution(n):
    answer = 0
    ternary = ""
    idx = 0

    while n//3 >= 1:                    # 3진법 변환
        remain = n % 3
        n //= 3
        ternary = str(remain) + ternary       
    ternary = str(n) + ternary
    
    for i in ternary:                   # 3진법 reverse -> 10진법 변환
        answer += int(i)*(3**idx)
        idx += 1

    return answer

print(solution(n))