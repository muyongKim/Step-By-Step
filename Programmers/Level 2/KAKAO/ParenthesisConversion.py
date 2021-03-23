# 괄호 변환 2021/03/23
# Retry
# Input
p = "(())()"

def checkBalance(p):
    lcnt = 0
    rcnt = 0

    for v in p:
        if v == "(":
            lcnt += 1
        else:
            rcnt += 1
    
    if lcnt == rcnt:
        return True
    else:
        return False

def checkCorrect(p):
    lcnt = 0
    rcnt = 0
    
    for v in p:
        if v == "(":
            lcnt += 1
        else:
            rcnt += 1
        if rcnt > lcnt:
            return False
    
    return True

def solution(p):
    if not p or checkCorrect(p):
        return p

    for i in range(len(p)):
        if checkBalance(p[:i+1]):
            u, v = p[:i+1], p[i+1:]
            break
    
    if checkCorrect(u):
        return u + solution(v)
    else:
        newP = "(" + solution(v) + ")"
        u = u[1:-1]

        for u_ in u:
            if u_ == "(":
                newP += ")"
            elif u_ == ")":
                newP += "("
    
    return newP

    

    
    


print(solution(p))