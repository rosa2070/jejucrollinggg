import requests
from bs4 import BeautifulSoup
import datetime

class 사업명정리클래스:
    pass

url = 'http://www.jejuiucc.or.kr/default/Bd/list.php?btable=notice'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

사업정리 = []
사업명 = soup.select('.jn_title')
날짜 = soup.select('.jn_date')
for 사업, 개별날짜 in zip(사업명, 날짜):
    # print(사업, 개별날짜)
    사업정리.append(사업명정리클래스())
    사업정리[-1].name = 사업.a['title'].strip()
    사업정리[-1].date = 개별날짜.text.strip()
    사업정리[-1].기관 = '제주산학융합원'

# 사업정리[-1].name
# 사업정리[-1].date
# 사업정리[-1].기관

date = datetime.datetime.today()

키워드 = [
    '채용',
    '지원',
    '오피스'
]

with open(f'/workspace/jejucr/{date.year}_{date.month}_{date.day}_{date.hour}_{date.minute}.txt', 'w') as f:
    result = ''
    for i in 사업정리:
        result += f'{i.기관}, {i.name}, {i.date}\n'
    f.write(result