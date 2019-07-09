# random 가져오기
import random
# 1~45 리스트 만들기
numbers = range(1, 46)
# 무작위 숫자 6개 뽑아오기
lotto = random.sample(numbers, 6)
# 뽑아온 숫자를 정렬 상태로 출력하기
print(sorted(lotto))
# 숫자를 정렬해서 저장 후 출력
# lotto.sort()
# print(lotto)