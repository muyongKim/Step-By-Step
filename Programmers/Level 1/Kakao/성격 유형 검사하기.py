# 22.10.13
# 2022 KAKAO TECH INTERNSHIP
# input
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]


def solution(survey, choices):
    answer = ""
    score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    indicator = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]

    for idx, c in enumerate(choices):
        if c > 4:
            score[survey[idx][1]] += c - 4
        elif c < 4:
            score[survey[idx][0]] += 4 - c
        else:
            continue

    for i in indicator:
        if score[i[0]] >= score[i[1]]:
            answer += i[0]
        else:
            answer += i[1]

    return answer

print(solution(survey, choices))