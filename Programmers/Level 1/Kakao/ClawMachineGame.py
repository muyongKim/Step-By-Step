# 크레인 인형뽑기 게임 2019 카카오 개발자 겨울 인턴쉽
# Input
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    stack = []
    cnt = 0
    board = list(map(list,zip(*board)))
    
    for m in moves:
        for n in board[m-1]:
            if n != 0:
                stack.append(n)
                board[m-1].remove(n)
                break

        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                cnt += 2

    return cnt

print(solution(board, moves))
