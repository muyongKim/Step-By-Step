# 오픈채팅방 2021/03/23
# Input
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    tmp = []
    userId = {}

    for r in record:
        tmp.append(r.split())

    for words in tmp:
        if words[0] == "Enter" or words[0] == "Change":
            userId[words[1]] = words[2]

    for words in tmp:
        if words[0] == "Enter":
            answer.append(userId[words[1]]+"님이 들어왔습니다.")
        elif words[0] == "Leave":
            answer.append(userId[words[1]]+"님이 나갔습니다.")
    
    return answer

print(solution(record))