# 22/02/22
# String
# Input
text = " practice   makes   perfect"

def solution(text):
    space = text.count(" ")
    arr = text.split()

    if len(arr) == 1:
        return "".join(arr) + " " * space
    else:
        end = space % (len(arr)-1)
        text = str(" " * (space//(len(arr)-1))).join(arr) + " " * end
        return text

print(solution(text))
# Runtime: 39 ms, faster than 57.99% of Python3 online submissions for Rearrange Spaces Between Words.
# Memory Usage: 14 MB, less than 61.18% of Python3 online submissions for Rearrange Spaces Between Words.