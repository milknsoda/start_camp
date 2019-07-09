import requests
from bs4 import BeautifulSoup

# 1. url 설정
url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
# 2. 요청 보내기
reponse = requests.get(url).text
# 3. HTML 문서로 바꾸기
soup = BeautifulSoup(reponse, 'html.parser')
# 4. 원하는 내용 선택자로 뽑아내기
table = soup.select('body > div > table > tbody > tr')
# body > div > table > tbody > tr:nth-child(1) > td.sale
for tr in table:
    print(tr.select_one('td.tit').text.strip(), tr.select('td.sale')[0].text) 
    # select는 무조건 list로 반환, select로 가져오는 정보가 하나의 원소만을 가지는 것이 확실할 경우에는 select_one을 사용
    # .strip()은 좌우의 공백을 제거
