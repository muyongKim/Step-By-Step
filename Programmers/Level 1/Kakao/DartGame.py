# 다트 게임 2018 KAKAO BLIND RECRUITMENT
# Input
dartResult = '1D2S#10S'

def solution(dartResult):
    answer = 0
    start = 0
    exScore = 0
    result = []

    for i in range(1,len(dartResult)):
        if dartResult[i].isdigit():
            if i - start == 1:
                continue
            result.append(dartResult[start:i])
            start = i
    result.append(dartResult[start:])

    for r in result:
        for i in range(1,len(r)):
            if r[i] == 'S':
                score = int(r[0])
            elif r[i] == 'D':
                score = int(r[0])*int(r[0])
            elif r[i] == 'T':
                score = int(r[0])*int(r[0])*int(r[0])
            elif r[i] == '*':
                score *= 2
                exScore *= 2
            elif r[i] == '#':
                score = -(score)
        answer += exScore
        exScore = score
    answer += exScore

    return answer
print(solution(dartResult))