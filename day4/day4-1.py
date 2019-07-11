"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
sume = 0
for s in score.values():
    sume = sume + s
average = sume / len(score)
print(f'평균: {average}')

# 풀이 : 반복문
result = 0
count = 0
for score_value in score.values():
    # result = result + score_value
    # count = count + 1
    result += score_value
    count += 1

# 풀이 : sum 함수 활용하기
result = sum(score.values())
count = len(score)
print(result / len(score))

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
result = 0
for key in scores:
    sumee = 0
    for score in scores[key]:
        sumee = sumee + scores[key][score]
    sumee = sumee / len(scores[key])
    print(f'{key}의 평균 : {sumee:.1f}')
    result = result + sumee
print(f'전체평균 : {result / len(scores):.1f}')

# 풀이
total_score = 0
count = 0
for per_scores in scores.values():
    for per_score in per_scores.values():
        total_score += per_score
        count += 1
print(total_score / count)


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
for ct in city:
    av = 0
    for tem in city[ct]:
        av += tem
    print(f'{ct} : {av/3:.2f}')


# 풀이
for name, temp in city.items():
    avg = sum(temp)/len(temp)
    print(f'{name} : {avg:.2f}') # f-string : 3.6+
    print('{0} : {1:.2f}'.format(name, avg)) # format-string
    print(name,':',avg)



# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

# tem_max = []
# tem_min = []
# for ct in city:
#     tem_tot = []
#     for tem in city[ct]:
#         tem_tot.append(tem)
#     tem_max.append((ct, max(tem_tot)))
#     tem_min.append((ct, min(tem_tot)))
# print(tem_max, tem_min)


# max_temp = []
# min_temp = []
# for i in tem_max:
#     max_temp.append(i[1])
# for i in tem_min:
#     min_temp.append(i[1])
# result_x = max(max_temp)
# result_n = min(min_temp)

tem_max = []
tem_min = []
for i in city:
    tem_max.append(max(city[i]))
    tem_min.append(min(city[i]))
print('3일 중에 가장 더웠던 곳 : ', end='')
for i in city:
    if max(tem_max) in city[i]:
        print(i, end=' ')
print('3일 중에 가장 추웠던 곳 : ', end='')
for i in city:
    if min(tem_min) in city[i]:
        print(i, end=' ')


# 풀이
min_temp = 0
max_temp = 0
min_city = ''
max_city = ''
count = 0
# 모든 지역의 온도를 모두 확인하면서,
for name, temp in city.items():
    # 첫번째 반복때는 모두 다 저장해!
    if count == 0:
        min_city = name
        max_city = name
        min_temp = min(temp)
        max_temp = max(temp)
        count += 1
# 가장 추우면, 해당 도시와 기온을 기록
    if min(temp) < min_temp:
        min_city = name
        min_temp = min(temp)
# 더울 때도, 해당 도시와 기온을 기록
    if max(temp) > max_temp:
        max_city = name
        max_temp = max(temp)
print(f'추운 곳은 {min_city}, 더운 곳은 {max_city}')



# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
for ct in city:
    if ct == '서울':
        if 2 in city[ct]:
            print('서울은 2도였던 적이 있다.')
        else:
            print('서울은 2도였던 적이 없다.')


# 풀이
if 2 in city['서울']:
    print('네')
else:
    print('아니오')
