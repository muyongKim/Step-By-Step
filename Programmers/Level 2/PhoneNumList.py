# 전화번호 목록 2021/05/02
# Input
phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True

print(solution(phone_book))
