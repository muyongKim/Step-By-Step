# 22.11.10
# https://school.programmers.co.kr/learn/courses/30/lessons/131127
# input
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]


def solution(want, number, discount):
    answer = 0

    for i in range(len(discount) - 9):
        flag = True
        tmp = discount[i:i + 10]

        for j in range(len(want)):
            if tmp.count(want[j]) < number[j]:
                flag = False
                break

        if flag:
            answer += 1

    return answer


print(solution(want, number, discount))