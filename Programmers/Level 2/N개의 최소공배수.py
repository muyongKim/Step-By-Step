# N개의 최소공배수 2021/03/02
# https://school.programmers.co.kr/learn/courses/30/lessons/12953
# Input
arr = [2,6,8,14]

# from math import gcd
#
# def solution(arr):
#     answer = 0
#     arr.sort()
#     for i in range(len(arr)-1):
#         arr[i+1] = int(arr[i] * (arr[i+1]/gcd(arr[i],arr[i+1])))
#     answer = arr[-1]
#
#     return answer


# 22.11.18
from math import gcd


def solution(arr):
    answer = 0
    a = arr[0]

    for b in arr[1:]:
        answer = (a * b) // gcd(a, b)
        a = answer

    return answer


print(solution(arr))