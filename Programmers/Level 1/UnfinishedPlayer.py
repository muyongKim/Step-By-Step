# 완주하지 못한 선수 21/01/29
# Input
participation = ["leo","kiki","eden"]
completion = ["eden","kiki"]

def solution(participation, completion):
    participation.sort()
    completion.sort()
    completion.append("")                           # 두 배열 길이는 1 차이나므로 마지막 인덱스를 비교하기 위함.

    for p,c in zip(participation,completion):
        if p != c:
            return p
    
print(solution(participation,completion))