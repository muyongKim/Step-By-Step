# 후보키 2019 kakao blind recruitment 2021/04/04
# Input
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

def solution(relation):
    # 1. 속성 하나에 속하는 튜플을 픽해 새로운 배열 생성
    # 2. 생성한 배열에서 중복 개수 카운트
    # 3. 중복값 없으면 -> 후보키
    # 4. 중복값 있으면 새로운 컬럼에 속하는 튜플을 배열에 추가
    # 5. 하나씩 반복??????