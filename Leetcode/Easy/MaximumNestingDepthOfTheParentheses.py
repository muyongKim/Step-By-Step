# 22/01/16
# String, Stack
# Input
s = "()"

def solution(s):
    left, right = [], []
    depth = 0

    for i in range(len(s)):
        if s[i] == "(":
            left.append(s[i])
        elif s[i] == ")":
            right.append(s[i])

        depth_now = len(left) - len(right)
        
        if depth_now > depth:
            depth = depth_now
    
    return depth

print(solution(s))
            