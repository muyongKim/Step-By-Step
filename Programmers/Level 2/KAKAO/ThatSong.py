# 방금그곡 2018 kakao blind recruitment
# Input
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def solution(m,musicinfos):
    dic = {}

    for info in musicinfos:
        info = info.split(',')
        hour = int(info[1][:2]) - int(info[0][:2])
        minute = int(info[1][3:]) - int(info[0][3:])
        if minute < 0:
            minute += 60
        
        playtime = hour*60 + minute
        info.append(playtime)
        
        melody = ''
        while playtime:
            for i in range(len(info[3])):
                if not i == len(info[3]) - 1 and info[3][i+1] == '#':
                    melody += info[3][i:i+2]
                else:
                    if info[3][i] == '#':
                        continue
                    melody += info[3][i]
                playtime -= 1

                if playtime == 0:
                    break
        
        if m in melody:
            if melody.find(m) + len(m) < len(melody) and melody[melody.find(m) + len(m)] == '#':
                melody = melody[len(m)+1:]
                continue
            else:
                dic[info[2]] = info[4]

    if not dic:
        return "(None)"
    else:
        return max(dic,key=dic.get)

print(solution(m,musicinfos))