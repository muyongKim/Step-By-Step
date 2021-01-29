# 문자열 내 p와 y의 개수 2021/01/25
# Input
s = "pPoooyY"

def solution(s):
    s = s.lower()
    pNum = s.count('p')
    yNum = s.count('y')
    
    if pNum == yNum:
        return True
    else: return False

print(solution(s))