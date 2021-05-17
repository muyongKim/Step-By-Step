# 완주하지 못한 선수 21/01/30
# Input
participation = ["leo","kiki","eden"]
completion = ["eden","kiki"]

def solution(participation, completion):
    participation.sort()
    completion.sort()
    completion.append("")                           
    for p,c in zip(participation,completion):
        if p != c:
            return p
    
print(solution(participation,completion))