# 메뉴 리뉴얼 2021 KAKAO BLIND RECRUITMENT 2021/02/06
# Input
orders = ["ABCDE","AC","CDE","ACDE","BCFG","ACDEH"]
course = [2,3,4]    

from itertools import combinations
from itertools import chain

def solution(orders,course):
    comb_list = []
    temp = []
    for j in course:
        for i in orders:
            temp.append(["".join(v) for v in list(combinations(i,j))])
    comb_list.append(temp)
    print(comb_list)

solution(orders,course)