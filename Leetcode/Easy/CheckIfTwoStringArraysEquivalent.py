# 22/01/16
# Array, String
# Input
word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]

def solution(word1, word2):
    if "".join(word1) == "".join(word2):
        return True
    else:
        return False

print(solution(word1, word2))