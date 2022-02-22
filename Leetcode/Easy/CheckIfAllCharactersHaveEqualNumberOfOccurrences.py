# 22/02/22
# Hash Table, String, Counting
# Input
s = "aaabb"

from collections import Counter

def solution(s):
    dict = Counter(s)

    if len(set(dict.values())) > 1:
        return False
    else:
        return True

print(solution(s))
# Runtime: 54 ms, faster than 36.75% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences.
# Memory Usage: 13.9 MB, less than 70.97% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences.