# 22.10.13
# 2022 KAKAO BLIND
# input
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3


def solution(id_list, report, k):
    answer = []
    banned = []
    report_dict = dict.fromkeys(id_list)

    # 딕셔너리 초기화
    for key in report_dict.keys():
        report_dict[key] = {'count': 0, 'report': []}

    # 유저가 신고당한 수, 신고한 유저 저장
    for r in list(set(report)):
        r = r.split()
        report_dict[r[0]]['report'].append(r[1])
        report_dict[r[1]]['count'] += 1

    # 유저 정지
    for key in report_dict.keys():
        if report_dict[key]['count'] >= k:
            banned.append(key)

    # 신고한 유저에서 정지당한 유저 카운트
    for key in report_dict.keys():
        cnt = 0
        for user in report_dict[key]['report']:
            if user in banned:
                cnt += 1
        answer.append(cnt)

    return answer

print(solution(id_list, report, k))