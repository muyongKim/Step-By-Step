# 위장 2021/02/01
# Input
clothes = [["yellow_hat","headgear"],["blue_sunglasses","eyewear"],["green_turban","headgear"]]

def solution(clothes):
    cDict = {}
    answer = 1
    for kind in clothes:
        if kind[1] in cDict:
            cDict[kind[1]] += 1
        else:
            cDict[kind[1]] = 1

    for v in cDict.values():
        answer *= (v+1)             # 조합 = (headgear+1)*(eyewear+1) - 1(모두 안 입는 경우)

    return answer-1

print(solution(clothes))