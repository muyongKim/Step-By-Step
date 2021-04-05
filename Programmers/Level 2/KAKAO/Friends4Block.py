# 프렌즈4블록 2018 kakao blind recruitment 2021/04/05
# Input
m, n = 6,6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def checkblock(m, n, b):
    sameBlock = []

    for i in range(n-1):
        for j in range(m-1):
            if b[i][j].isalpha() and b[i][j] == b[i][j+1] and b[i][j] == b[i+1][j] and b[i][j] == b[i+1][j+1]:
                sameBlock.append((i,j))
                sameBlock.append((i,j+1))
                sameBlock.append((i+1,j))
                sameBlock.append((i+1,j+1))

    sameBlock = list(set(sameBlock))
    return sameBlock

def solution(m, n, board):
    b = []
    cnt = 0

    # 오른쪽 90도 회전
    for i in range(n):
        b.append([])
        for j in range(1,m+1):
            b[i].append(board[-j][i])

    while True:
        sameBlock = checkblock(m,n,b)

        if not sameBlock:
            return cnt
        
        sameBlock.sort()
        sameBlock.reverse()

        for idx in sameBlock:
            b[idx[0]].pop(idx[1])
            b[idx[0]].append("0")
            cnt += 1

print(solution(m,n,board))