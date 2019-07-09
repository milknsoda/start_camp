# window - cp949 (encoding)
# mac/web... - utf-8
with open('ssafy_with.txt', 'r', encoding = 'utf-8') as f:
    # readlines는 라인을 각각 리스트의 원소로 하여 반환한다.
    lines = f.readlines()

for line in lines:
    print(line.strip()) # 양쪽에 있는 공백, 개행문자 모두 없애준다.

with open('ssafy.txt', 'r') as f:
    # read : 전체 내용을 하나의 string으로 반환한다.
    txt = f.read()

print(txt)
print(type(txt))