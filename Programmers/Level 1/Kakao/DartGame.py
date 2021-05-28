# 다트 게임 2018 KAKAO BLIND RECRUITMENT
# Input
result = '1D2S#10S'

def solution(dartResult):
    answer = 0
    num = 0
    tmp = []

    for i in range(len(result)):
        if result[i].isdigit():
            if result[i+1].isdigit():
                num = int(result[i] + result[i+1])
                continue
            else:
                if num == 10:
                    continue
                num = int(result[i])
                continue
        
        else:
            if result[i] == 'S':
                score = num
                if i != len(result) - 1 and result[i+1].isdigit():
                    tmp.append(score)
                    continue
            elif result[i] == 'D':
                score = num*num
                if i != len(result) - 1 and result[i+1].isdigit():
                    tmp.append(score)
                    continue
            elif result[i] == 'T':
                score = num*num*num
                if i != len(result) - 1 and result[i+1].isdigit():
                    tmp.append(score)
                    continue
            elif result[i] == '*':
                score *= 2
                if tmp:
                    tmp[-1] *= 2
                tmp.append(score)
            elif result[i] == '#':
                score = -(score)
                tmp.append(score)

    return answer
print(solution(result))