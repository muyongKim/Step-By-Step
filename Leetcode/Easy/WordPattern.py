# 22/02/23
# Hash Table, String
# Input
pattern = "aaaa"
s = "dog cat cat dog"

def solution(pattern, s):
    words = list(dict.fromkeys(s.split()))
    letter = list(dict.fromkeys(pattern))
    match = {}
    output = ""

    if len(words) != len(letter):
        return False

    for w, p in zip(words,letter):
        if w not in match:
            match[w] = p
    
    for w in s.split():
        output += match[w]
    
    if output != pattern:
        return False
    else:
        return True


print(solution(pattern,s))
# Runtime: 36 ms, faster than 68.83% of Python3 online submissions for Word Pattern.
# Memory Usage: 13.9 MB, less than 86.14% of Python3 online submissions for Word Pattern.