# JadenCase 문자열 만들기 2021/03/03
# Input
s = "for the last week"

def solution(s):
    answer = []
    tmp = s.split(" ")

    for word in tmp:
        answer.append(word.capitalize())
    
    return " ".join(answer)

print(solution(s))