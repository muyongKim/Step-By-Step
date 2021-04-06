# 후보키 2019 kakao blind recruitment 2021/04/04
# Input
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

from itertools import combinations

def solution(relation):
    key = []
    col = [n for n in range(len(relation[0]))]
    
    for n in range(1,len(col)+1):
        
        comb = list(combinations(col,n))
        
        for c in comb:
            check = []
            for r in relation:
                tmp = ""
                for v in c:
                    tmp += r[v]
                check.append(tmp)

            if len(check) == len(set(check)):
                flag = True
                
                for k in key:
                    if k & set(c) == k:
                        flag = False
                        break
                
                if flag:
                    key.append(set(c))

    return len(key)
            
print(solution(relation))