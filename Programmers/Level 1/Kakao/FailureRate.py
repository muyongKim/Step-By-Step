# 실패율 2019 kakao blind recruitment
# Input
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    stageFail = {}
    answer = []

    for i in range(1,N+1):
        tryUser = 0
        for s in stages:
            if i <= s:
                tryUser += 1
        if tryUser == 0:
            failRate = 0
        else:
            failRate = stages.count(i) / tryUser
        stageFail[i] = failRate
    
    return sorted(stageFail, key = lambda x: stageFail[x], reverse = True)
    
print(solution(N,stages))