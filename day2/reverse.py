# number.txt를 읽어서
# 리스트 (readlines)
with open('number.txt', 'r') as f:
    num = f.readlines()

print(num)
num.reverse() # == reversed(num)
# number_reverse.txt로 저장!
with open('number_reverse.txt', 'w') as f:
    for k in num:
        f.write(k)

# alt + 화살표 : 줄을 변경가능