# 가장 큰 정사각형 찾기 2021/03/15
# Retry
# Input
board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

def solution(board):
    answer = 0
    width_p = board[0].count(1)     # 가로 길이가 될 수 있는 행
    idx = []
    
    for i in range(len(board)):
        tmp = board[i].count(1)
        if tmp >= width_p and tmp <= len(board):
            width_p = tmp
            idx.append(i)

print(solution(board))