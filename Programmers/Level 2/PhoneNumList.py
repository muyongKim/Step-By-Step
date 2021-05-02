# 전화번호 목록 2021/05/02
# Input
phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    for i in range(len(phone_book)-1):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] in phone_book[j]:
                return False
    
    return True

print(solution(phone_book))