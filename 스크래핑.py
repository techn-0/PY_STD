import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.daum.net/ranking/boxoffice/yearly', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, li들을 불러오기
movies = soup.select('.entertain_type1 > #kakaoContent > #cMain > #mArticle > .box_g > .list_news > ul > li')

print(len(movies)) # 50

for movie in movies:
    print(movie)
#############################
# (입맛에 맞게 코딩)
#############################

# movies (li들) 의 반복문을 돌리기