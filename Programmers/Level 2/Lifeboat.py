# 구명보트 2021/03/02
# Input
people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    answer = len(people)
    people.sort(reverse = True)
    idx = 0
    min_p = len(people)-1

    while idx < min_p:
        if people[idx]+people[min_p] <= limit:
            min_p -= 1
            answer -= 1
        idx += 1
    
    return answer