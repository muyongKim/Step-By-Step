# 정수 내림차순으로 배치하기 2021/02/05
# Input
n = int(input())

def solution(n):
    n = str(n)
    n_list = [i for i in n]     # n_list = list(str(n))
    n_list.sort(reverse=True)
    return int("".join(n_list))

print(solution(n))