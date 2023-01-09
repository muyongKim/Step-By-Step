# 23.01.09
# https://school.programmers.co.kr/learn/courses/30/lessons/120907
# input
quiz = ["3 - 4 = -3", "5 + 6 = 11"]


def solution(quiz):
    answer = []

    for q in quiz:
        q = q.split()

        if q[1] == '+':
            if int(q[0]) + int(q[2]) == int(q[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(q[0]) - int(q[2]) == int(q[4]):
                answer.append('O')
            else:
                answer.append('X')

    return answer