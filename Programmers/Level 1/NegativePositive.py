# 음양 더하기 2021/05/07
# Input
absolutes = [4,7,12]
signs = [True, False, True]

def solution(absolutes, signs):
    answer = 0

    for num, sign in zip(absolutes,signs):
        if sign == True:
            answer += num
        else:
            answer -= num
    
    return answer

print(solution(absolutes,signs))