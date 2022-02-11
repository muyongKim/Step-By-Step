# 22/02/11
# String
# Input
s = "1111"

def solution(s):
    case1, case2 = 0, 0

    for i in range(0,len(s)):
        if i % 2 == 1 and s[i] != "1":
            s.replace(s[i], "1")
            case1 += 1
        elif i % 2 == 0 and s[i] != "0":
            s.replace(s[i],"0")
            case1 += 1

    for i in range(0,len(s)):
        if i % 2 == 1 and s[i] != "0":
            s.replace(s[i],"0")
            case2 += 1
        elif i % 2 == 0 and s[i] != "1":
            s.replace(s[i], "1")
            case2 += 1

    return min(case1, case2)
    # -> too much runtime
    # cnt = 0
    
    # for i in range(len(s)):
    #     if int(s[i]) == i % 2:
    #         cnt += 1
    # return min(cnt, len(s)-cnt)
    # -> faster


print(solution(s))