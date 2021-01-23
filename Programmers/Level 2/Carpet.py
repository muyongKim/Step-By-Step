# 카펫
# # Input
brown = 24
yellow = 24

def solution(brown,yellow):
    divisor = []

    for i in range(1, yellow+1):            # yellow의 약수
        if yellow % i == 0:                 # but 실행시간이 길어짐
            divisor.append(i)
    
    divisor.reverse()

    for n in range(0, int(len(divisor)/2)+1):
        if brown == 2*divisor[n] + 2*(yellow/divisor[n]+2):
            answer = [divisor[n]+2, int(yellow/divisor[n])+2]
            return answer

print(solution(brown,yellow))