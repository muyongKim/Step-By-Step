# x만큼 간격이 있는 n개의 숫자 2021/01/31
# Input
x = 2
n = 5

def solution(x,n):
    answer = []
    if x==0:                        # x = 0 일때 예외처리.
        for i in range(n):
            answer.append(x)
    else:
        answer = [v for v in range(x,x+x*n,x)]      # range의 arg3은 0이 올 수 없다.
    return answer

print(solution(x,n))