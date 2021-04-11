# 방금그곡 2018 kakao blind recruitment 2021/04/10
# Input
m = "ABC"
musicinfos = ["13:00,13:10,WORLD,ABC#ABC", "13:00,13:12,WORLD2,ABCDEF"]

def solution(m,musicinfos):
    dic = {}

    for info in musicinfos:
        info = info.split(',')

        # 재생시간 
        hour = int(info[1][:2]) - int(info[0][:2])
        minute = int(info[1][3:]) - int(info[0][3:])
        if minute < 0:
            minute += 60
            hour -= 1
        
        playtime = hour*60 + minute
        info.append(playtime)
        
        # 라디오에서 재생된 멜로디
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
        
        # 멜로디 비교
        while melody.find(m)+1:
            if melody.find(m) + len(m) < len(melody) and melody[melody.find(m) + len(m)] == '#':
                melody = melody[melody.find(m)+len(m)+1:]
                continue
            else:
                dic[info[2]] = info[4]
                break

    if not dic:
        return "(None)"
    else:
        return max(dic,key=dic.get)

print(solution(m,musicinfos))