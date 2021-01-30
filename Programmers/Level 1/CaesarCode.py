# 시저 암호 21/01/31
# Input
s = "a B z"
n = 4

def solution(s,n):
    answer = ''
    for char in s:
        if ord(char)+n>90 and char.isupper():       # 대문자 순환 Z -> A
            answer += chr(ord(char)+n-26)
        elif ord(char)+n>122 and char.islower():    # 소문자 순환 z -> a
            answer += chr(ord(char)+n-26)
        elif ord(char) == 32:                       # 공백
            answer += ' '
        else:
            answer += chr(ord(char)+n)
    return answer

print(solution(s,n))

# chr(): 아스키코드 -> 문자, ord(): 문자 -> 아스키코드