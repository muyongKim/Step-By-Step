# 23.01.06
# https://school.programmers.co.kr/learn/courses/30/lessons/136798
# input
number = 5
limit = 3
power = 2


def solution(number, limit, power):
    weaphons = []

    for n in range(1, number + 1):
        cnt = 0

        for i in range(1, int(n ** (1 / 2)) + 1):
            if n % i == 0:
                cnt += 1

                if (i ** 2) != n:
                    cnt += 1

        if cnt > limit:
            weaphons.append(power)
        else:
            weaphons.append(cnt)

    return sum(weaphons)


print(solution(number, limit, power))