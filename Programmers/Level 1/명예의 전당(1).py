# 23.01.05
# https://school.programmers.co.kr/learn/courses/30/lessons/138477
# input
k = 3
score = [10, 100, 20, 150, 1, 100, 200]


def solution(k, score):
    answer = []
    rank = []

    for s in score:
        rank.append(s)
        rank.sort()

        if len(rank) > k:
            rank = rank[1:k + 1]

        answer.append(rank[0])

    return answer


print(solution(k, score))