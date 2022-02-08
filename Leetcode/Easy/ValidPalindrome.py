# 22/02/08
# Two Pointers, String
# Input
s = " "

def solution(s):
    new_s = ""

    for c in s:
        if c.isalnum():
            new_s += c.lower()
    
    if new_s == new_s[::-1]:
        return True
    else:
        return False

print(solution(s))