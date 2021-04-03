# 뉴스 클러스터링 2018 kakao blind recruitment 2021/04/03
# Input
str1 = "aa1+aa2"
str2 = "AAAA12"

def make_set(str_, set_):
    for i in range(len(str_)-1):
        if str_[i].isalpha() and str_[i+1].isalpha():
            set_.append(str_[i]+str_[i+1])

def solution(str1, str2):
    set1, set2 = [], []
    u_tmp, i_tmp = [], []
    str1 = str1.lower()
    str2 = str2.lower()

    make_set(str1, set1)
    make_set(str2, set2)

    if not set1 and not set2:
        return 65536

    u_set = list(set(set1) | set(set2))
    i_set = list(set(set1) & set(set2))

    # 합집합
    for s in u_set:
        if set1.count(s) > 1 or set2.count(s) > 1:
            cnt = max(set1.count(s), set2.count(s))
            for i in range(cnt-1):
                u_tmp.append(s)

    for s in u_tmp:
        u_set.append(s)

    # 교집합
    for s in i_set:
        if set1.count(s) > 1 and set2.count(s) > 1:
            cnt = min(set1.count(s), set2.count(s))
            for i in range(cnt-1):
                i_tmp.append(s)
    
    for s in i_tmp:
        i_set.append(s)

    answer = int((len(i_set) / len(u_set)) * 65536)
    return answer

print(solution(str1, str2))