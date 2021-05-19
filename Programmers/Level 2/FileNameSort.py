# 파일명 정렬 2021/04/23
# Input
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def makeHeadNumber(file):
    h = 0

    for s in file:
        if s.isdigit():
            break
        h += 1

    head = file[:h].lower()

    number = file[h:h+5]
    n = 0

    for s in number:
        if not s.isdigit():
            break
        n += 1

    return [head, int(number[:n])]

def solution(files):
    files.sort(key = lambda x : makeHeadNumber(x))

    return files

print(solution(files))