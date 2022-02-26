# 22/02/26
# Input
words = ["a", "aa","a"]

from collections import Counter

def solution(words):
    length = len(words)
    words = Counter("".join(words))
    
    for n in words.values():
        if n % length != 0:
            return False
    return True

print(solution(words))
# Runtime: 81 ms, faster than 57.55% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
# Memory Usage: 14.2 MB, less than 67.61% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.