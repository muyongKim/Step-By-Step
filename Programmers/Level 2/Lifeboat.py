# 구명보트 2021/03/02
# Input
people = [90, 80, 70, 60, 60, 40, 40]
limit = 140

# 기존 코드가 더 효율적
# def solution(people, limit):
#     answer = len(people)
#     people.sort(reverse = True)
#     idx = 0
#     min_p = len(people)-1

#     while idx < min_p:
#         if people[idx]+people[min_p] <= limit:
#             min_p -= 1
#             answer -= 1
#         idx += 1
#     return answer

# Retry 2021/06/11
def solution(people, limit):
    answer = len(people)
    max_p = 0
    min_p = len(people)-1
    people.sort(reverse = True)

    while max_p < min_p:
        if people[max_p] <= limit/2:
            if int(len(people[max_p:min_p+1])/2) == len(people[max_p:min_p+1])/2:
                answer -= len(people[max_p:min_p+1])/2
            else:
                answer -= int((len(people[max_p:min_p+1])/2))
            return answer

        elif people[max_p] + people[min_p] <= limit:
            min_p -= 1
            answer -= 1
        max_p += 1
    return answer
print(solution(people, limit))