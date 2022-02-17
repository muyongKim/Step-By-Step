# 22/02/17
# Hash Table, String, Counting
# Input
ransomNote = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"

def solution(ransomNote, magazine):
    dict = {}

    for n in ransomNote:
        if n not in dict:
            dict[n] = 0
        dict[n] += 1
    
    for m in magazine:
        if m in dict and dict[m] != 0:
            dict[m] -= 1
        if sum(dict.values()) == 0:
            return True
    return False

print(solution(ransomNote, magazine))
# Runtime: 176 ms, faster than 5.09% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.2 MB, less than 83.17% of Python3 online submissions for Ransom Note.

# 문자열, list 요소 카운팅 -> Counter 사용!!