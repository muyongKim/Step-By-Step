# 가운데 글자 가져오기
# Input
s = 'abcde'

def solution(s):
    answer = ''
    idx = int(len(s)/2)
    if (len(s) % 2 == 0):
        answer = s[(idx -1)] + s[idx]
    else:
        answer = s[idx]
    return answer

print(solution(s))