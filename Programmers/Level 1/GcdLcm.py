# 최대공약수와 최소공배수 2021/03/05
# Input
n, m = 2,5

from math import gcd

def solution(n,m):
    answer = []
    tmp = gcd(n,m)
    answer.append(tmp)

    lcm = int(tmp * (n/tmp) * (m/tmp))
    answer.append(lcm)

    return answer

print(solution(n,m))