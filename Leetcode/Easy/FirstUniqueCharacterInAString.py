# 22/02/09
# Hash Table, String, Queue, Counting
# Input
s = "loveleetcode"

def solution(s):
    dict = {}
    output = 0

    for c in s:
        if c not in dict:
            dict[c] = 0
        dict[c] += 1
    
    keys = list(dict.keys())

    for k in keys:
        if dict[k] > 1:
            del(dict[k])
    
    if dict:
        output = s.find(str(list(dict.keys())[0]))
    else:
        output = -1

    return output

print(solution(s))

# colletctions 모듈의 counter
# -> 문자열, list의 요소를 카운팅하여 많은 순으로 딕셔너리 형태로 리턴
# from collections import Counter

# def solution(s):
#     counts = Counter(s)

#     # .items() -> 튜플 형태, 저장된 순서대로 리턴
#     for key, value in counts.items():
#         if value == 1:
#             return s.index(key)
#     return -1
# print(solution(s))