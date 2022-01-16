# 22/01/16
# String, Stack
# Input
s = "()"

def solution(s):
    left, right = 0, 0
    depth = 0

    for i in range(len(s)):
        if s[i] == "(":
            left += 1
        elif s[i] == ")":
            right += 1
        
        depth = max(depth, left - right)

    return depth
    
print(solution(s))
            