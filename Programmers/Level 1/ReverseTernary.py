'''
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
'''
# Input
n = 125

def solution(n):
    ternary = ""
    answer = 0
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