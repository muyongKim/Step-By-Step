# 영어 끝말잇기 2021/03/23
# Input
n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

def check_loser(n, cnt):
    answer = []
    loser = cnt % n

    if loser == 0:
        loser = n
        loop = cnt // n
    else:
        loop = cnt // n + 1

    answer.append(loser)
    answer.append(loop)

    return answer

def solution(n, words):
    passed = []
    answer = [0, 0]
    cnt = 0

    for w in words:
        cnt += 1
        if not passed or passed[-1][-1] == w[0]:
            if w in passed:
                return check_loser(n, cnt)
            passed.append(w)
        elif w[0] != passed[-1][-1]:
            return check_loser(n, cnt)

    return answer

print(solution(n, words))