# 다트 게임 2018 KAKAO BLIND RECRUITMENT
# Input
result = '1D#2S*3S'

def solution(result):
    scoreList = []
    score = 0
    flag = False
    result = result.replace('10','a')

    for r in result:
        if r in 'SDT':
            if r == 'D':
                score *= score
            elif r == 'T':
                score = score * score * score
        elif r in '*#':
            if r == '*':
                score *= 2
                if scoreList:
                    scoreList[-1] *= 2
            else:
                score = -(score)
        else:
            if flag:
                scoreList.append(score)
            if r == 'a':
                score = 10
            else:
                score = int(r)
            flag = True

    scoreList.append(score)
    answer = sum(scoreList)
    return answer

print(solution(result))