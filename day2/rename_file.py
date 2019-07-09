import os

# 1. dummy 폴더로 들어간다.
os.chdir('./dummy')
print(os.getcwd())

# 2. 하나씩 파일명을 변경한다. -> 반복문
files = os.listdir('.')
# print(files)
print(type(files))
# for file in files:
#     os.rename(file, f'SAMSUNG_{file}') # (원래 파일명, 바꿀 파일명)

for file in files:
    os.rename(file, file.replace('SAMSUNG', 'SSAFY'))

# for file in files:
#     os.rename(file, file.replace('SSAFY_',''))