# 예산
# Input
d = [1,2,4]
budget = 8

def solution(d, budget):
    answer = 0
    money = 0
    d.sort()
    for dep in d:
        answer+=1
        money+=dep              
        if money>budget:
            return answer-1
    return answer

print(solution(d,budget))