# 22.11.12
# https://school.programmers.co.kr/learn/courses/30/lessons/135808
# input
k, m = 3, 4
score = [1, 2, 3, 1, 2, 3, 1]


def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    for i in range(len(score) // m):
        box = sorted(score[i * m:i * m + m])
        answer += box[0] * m

    return answer


print(solution(k,m,score))