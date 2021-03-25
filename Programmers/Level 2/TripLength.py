# 방문 길이 2021/03/25
# Input
dirs = "LR"

def solution(dirs):
    answer = 0
    loc = [0, 0]
    path = []

    for d in dirs:
        line = []
        line.append([loc[0],loc[1]])

        if d == "U":
            if loc[1] == 5:
                continue
            loc[1] += 1
        elif d == "D":
            if loc[1] == -5:
                continue
            loc[1] -= 1
        elif d == "R":
            if loc[0] == 5:
                continue
            loc[0] += 1
        elif d == "L":
            if loc[0] == -5:
                continue
            loc[0] -= 1

        line.append([loc[0],loc[1]])
        line.sort()

        if line not in path:
            path.append(line)

    answer = len(path)
    return answer

print(solution(dirs))
