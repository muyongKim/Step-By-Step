# 최솟값 만들기 2021/01/29
# Input
A = [1,2]
B = [3,4]

# def solution(a,b):
#     answer = 0
#     a = sorted(a)
#     b = sorted(b)
#     c = a+b

#     if min(c) in a:
#         for i in range(0,len(a)):
#             answer += a[i]*b[len(b)-1-i]
#     else:
#         for j in range(0,len(a)):
#             answer += b[j]*a[len(a)-1-j]
#     return answer

# A와 B는 길이가 같이 때문에 위 코드처럼 최솟값이 존재하는 배열을 찾을 필요가 없음.

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for a,b in zip(A,B):        # zip(A,B)를 통해 여러 인자를 가져올 수 있음.
        answer += a*b
    return answer

print(solution(A,B))