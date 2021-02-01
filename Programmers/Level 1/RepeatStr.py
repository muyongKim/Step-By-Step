# 수박수박수박수박수박수? 2021/02/02
# Input
n = 4

def solution(n):
    word = "수박"
    answer = ""
    for i in range(n):
        answer += word[i%2]
    return answer

print(solution(n))