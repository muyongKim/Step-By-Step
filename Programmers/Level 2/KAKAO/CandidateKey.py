# 후보키 2019 kakao blind recruitment 2021/04/04
# Input
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

def solution(relation):
    key = []
    # 모든 단일 속성 후보키 체크
    for i in range(len(relation[0])):
        tmp = []
        for j in range(len(relation)):
            tmp.append(relation[j][i])
        if len(tmp) == len(set(tmp)):
            key.append(i)
    print(key)

print(solution(relation))