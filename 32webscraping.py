# 웹 크롤링과 스크래핑
# 크롤링 : 웹 상의 정보를 탐색하고 수집하는 행위
# 스크래핑 : 특정 웹사이트에 필요한 정보를 추출하는 것


import re  # 정규표현식 Regualr Expression
import csv
import json
from collections import OrderedDict
import requests
# pip install beautifulsoup4 터미널에서 설치해야함
from bs4 import BeautifulSoup

# 한빛 미디어 사이트의 베스트셀러 페이지에서 도서 정보 추출
url = 'https://www.hanbit.co.kr/store/books/bestseller_list.html'

# 웹사이트 접속 후 해당 페이지의 내용을 불러옴
res = requests.get(url)
print(res.text[:300])

# 불러온 내용을 분석하기 쉽게 beautifulsoap 객체로 초기화 - parsing
html = BeautifulSoup(res.text, 'html.parser')
print(html.title)

# 도서 정보(도서명, 저자, 가격) 추출
titles = []
writers = []
prices = []

# 도서명 추출
for title in html.select('p.book_tit a'):
    # print(title.text)
    titles.append(title.text)
print(titles)

# 저자 추출
for writer in html.select('p.book_writer'):
    # print(title.text)
    writers.append(writer.text)
print(writers)

# 가격 추출
# re.sub(찾을 문자열, 바꿀 문자열, 대상)
for price in html.select('span.price'):
    # print(title.text)
    price = re.sub(',', '', price.text)
    price = re.sub('원', '', price)
    prices.append(price)
print(prices)

# 스크래핑한 도서목록을 json형식으로 재구성
allbooks = OrderedDict()
books = []

for i in range(len(titles)):
    book = OrderedDict()
    book['title'] = titles[i]
    book['writer'] = writers[i]
    book['price'] = prices[i]
    books.append(book)

allbooks['books'] = books

# 생성한 json 객체를 파일로 저장
with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(allbooks, f, ensure_ascii=False)

# 파일에 저장된 json객체를 메모리로 불러옴
with open('books.json',  encoding='utf-8') as f:
    jbooks = json.load(f)

# 베스트셀러 검색 : get(키)
jbooks.get('books')
jbooks.get('books')[:5]
jbooks.get('books')[0].get('title')
jbooks.get('books')[1].get('title')
jbooks.get('books')[2].get('title')

# 도서정보를 csv 형식으로 저장하기
with open('books.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)   #csv 파일 저장을 위한 초기화
    for i in range(len(titles)):
        book = [titles[i], writers[i], prices[i]]
        writer.writerow(book)






































































