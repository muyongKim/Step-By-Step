# 22/02/10
# Two Pointers, String
# Input
s = "Let's take LeetCode contest"

def solution(s):
    s = s.split()

    for i in range(len(s)):
        s[i] = s[i][::-1]
    
    return " ".join(s)

print(solution(s))