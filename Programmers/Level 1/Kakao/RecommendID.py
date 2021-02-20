# 신규 아이디 추천 2021/02/20
# Retry
# Input
new_id = "=.="

def solution(new_id):
    ID = []

    # step 1
    new_id = new_id.lower()
    
    # step 2
    for i in new_id:
        if not 97 <= ord(i) <= 122 and not 48 <= ord(i) <= 57 and not ord(i) == 45 and not ord(i) == 46 and not ord(i) == 95:
            new_id = new_id.replace(i,"")
    print(new_id)

    # step 3
    for idx, char in enumerate(new_id):
        if char == '.' and idx < len(new_id) -1 and new_id[idx+1] == '.':
            continue
        else:
            ID.append(char)
    print("".join(ID))

    # step 4
    if ID[0] == '.':
        ID.pop(0)
    if ID and ID[-1] == '.':
        ID.pop()
    print("".join(ID))

    # step 5
    if len(ID) == 0:
        ID.append('a')
    print("".join(ID))

    
    # step 6
    if len(ID) >= 16:
        ID = ID[0:15]
        if ID[0] == '.':
            ID.pop(0)
        if ID[-1] == '.':
            ID.pop()
    print("".join(ID))

    # step 7
    if len(ID) <= 2:
        while len(ID) < 3:
            ID.append(ID[-1])
    
    return "".join(ID)

print(solution(new_id))