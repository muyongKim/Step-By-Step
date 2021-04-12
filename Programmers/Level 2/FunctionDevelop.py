# 기능개발 2021/04/12
# Input
progresses = [93,30,55]
speeds = [1,30,5]

def solution(progresses, speeds):
    publish = []
    progresses.reverse()
    speeds.reverse()

    while progresses:
        finished = []
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        if progresses[-1] >= 100:
            while True:
                finished.append(progresses.pop())
                speeds.pop()
                if not progresses or progresses[-1] < 100:
                    break
        
        if finished:
            publish.append(len(finished))
    
    return publish

print(solution(progresses,speeds))