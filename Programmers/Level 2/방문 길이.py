# https://school.programmers.co.kr/learn/courses/30/lessons/49994
# Input
dirs = "LR"

# 21.03.25
# def solution(dirs):
#     answer = 0
#     loc = [0, 0]
#     path = []
#
#     for d in dirs:
#         line = []
#         line.append([loc[0],loc[1]])
#
#         if d == "U":
#             if loc[1] == 5:
#                 continue
#             loc[1] += 1
#         elif d == "D":
#             if loc[1] == -5:
#                 continue
#             loc[1] -= 1
#         elif d == "R":
#             if loc[0] == 5:
#                 continue
#             loc[0] += 1
#         elif d == "L":
#             if loc[0] == -5:
#                 continue
#             loc[0] -= 1
#
#         line.append([loc[0],loc[1]])
#         line.sort()
#
#         if line not in path:
#             path.append(line)
#
#     answer = len(path)
#     return answer

# 22.10.28
def solution(dirs):
    command = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    path = set()

    for d in dirs:
        nx = x + command[d][0]
        ny = y + command[d][1]

        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue

        path.add((x, y, nx, ny))
        path.add((nx, ny, x, y))
        x, y = nx, ny

    return len(path) // 2


print(solution(dirs))
