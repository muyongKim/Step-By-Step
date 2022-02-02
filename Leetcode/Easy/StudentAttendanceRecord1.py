# 22/02/02
# String
# Input
s = "PPALLP"

def solution(s):
    if s.count("A") >= 2 or "LLL" in s:
        return False
    else:
        return True

print(solution(s))