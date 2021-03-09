# 땅따먹기 2021/02/23
# Retry
# Input
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):
    score_1 = max(land[0])
    idx = land[0].index(score_1)
    land.remove(land[0])
    sum = score_1

    for score in land:
        max_score = max(score)
        max_idx = score.index(max_score)

        if idx == max_idx:
            score.remove(max_score)
            max_score = max(score)
            idx = score.index(max_score)

        sum += max_score
    return sum

print(solution(land))