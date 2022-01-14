# 숫자 문자열과 영단어 2022/01/14
# Input
s = "one4seveneight"

def solution(s):
    word = { 0 : "zero", 1 : "one",  2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six",
            7 : "seven", 8 : "eight", 9 : "nine"}

    for i in range(len(word)):
        if word[i] in s:
            s = s.replace(word[i], str(i))
        
        if s.isdigit():
            break
    
    return int(s)

print(solution(s))
            