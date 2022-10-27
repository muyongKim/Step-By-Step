# 22.10.28
# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# input
skill, skill_trees = 'CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']


def solution(skill, skill_trees):
    answer = 0

    for s_tree in skill_trees:
        s_tree = list(s_tree)
        tmp = ''

        for s in s_tree:
            if s in skill:
                tmp += s

        if tmp == skill[:len(tmp)]:
            answer += 1

    return answer


print(solution(skill, skill_trees))