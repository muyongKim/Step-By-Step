# 최댓값과 최솟값 2021/04/30
# Input
s = '-1 -2 -3 -4'

def solution(s):
    answer = ''

    tmp = list(map(int, s.split()))
    print(tmp)
    answer = str(min(tmp)) + ' ' + str(max(tmp))

    return answer

print(solution(s))