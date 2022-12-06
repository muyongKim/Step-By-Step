# 22.12.06
# https://school.programmers.co.kr/learn/courses/30/lessons/140108?language=python3
# input
s = 'banana'

def solution(s):
    answer = 0
    x_cnt, other_cnt = 0, 0

    for ch in s:
        if x_cnt == other_cnt:
            answer += 1
            x = ch

        if ch == x:
            x_cnt += 1
        else:
            other_cnt += 1

    return answer


print(solution(s))