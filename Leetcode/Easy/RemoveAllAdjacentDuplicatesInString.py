# 22/02/25
# String, Stack
# Input
s = "abbbaca"

def solution(s):
    stack = []

    for c in s:
        if not stack:
            stack.append(c)
            continue
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    return "".join(stack)

print(solution(s))
# Runtime: 68 ms, faster than 97.70% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.9 MB, less than 56.80% of Python3 online submissions for Remove All Adjacent Duplicates In String.