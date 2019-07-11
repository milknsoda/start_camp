import random
import requests
import pprint

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
# 1. 요청
# json -> 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
# 응답 (HTML, XML, JSON)
response = requests.get(url).json()
# pprint.pprint(response)
# print(type(response))

# # 당첨번호 6개 + 보너스 번호
# win_lotto = []
# bonus = response['bnusNo']
# for i in range(1, 7):
#     win_lotto.append(response[f'drwtNo{i}'])

# 몇개 맞았는지 확인
# 1. 반복문으로 확인
# matched = 0
# for num in my_lotto:
#     if num in win_lotto:
#         matched += 1
# 2. 교집합으로 확인
# matched = len(set(win_lotto) & set(my_lotto))

# 몇개 맞았는지를 바탕으로 출력
# if matched == 6:
#     print('1등')
# elif matched == 5 and bonus in my_lotto:
#     print('2등')
# elif matched == 5:
#     print('3등')
#     ...


# a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
result = [0, 0, 0, 0, 0]

for i in range(10000000):
    nums = {}
    my_lotto = random.sample(range(1, 46), 6)
    for key, value in response.items():
        if 'drwtNo' in key:
            nums[value] = '당첨번호'
        if 'bnusNo' in key:
            nums[value] = '보너스번호'

    count = 0
    bonus = 0
    for i in my_lotto:
        for num in nums:
            if i == int(num):
                count += 1
            if nums[num] == '보너스번호':
                bonus += 1

    if count == 3:
        # print('5등!')
        # e += 1
        result[4] += 1
    elif count == 4:
        # print('4등!')
        # d += 1
        result[3] += 1
    elif count == 5:
        # print('3등!')
        # c += 1
        result[2] += 1
    elif count == 5 and bonus == 1:
        # print('2등!!!')
        # b += 1
        result[1] += 1
    elif count >= 6:
        # print('1등!!!!!')
        # a += 1
        result[0] += 1
    else:
        # print('꽝!!')
        # f += 1
        None
    print(result, end='\r')
print('끝')
print(sum(result))
