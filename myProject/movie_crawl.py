import requests
from bs4 import BeautifulSoup
import re
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from urllib.parse import urljoin
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myProject.settings")
import django
django.setup()

from movie.models import Movieinfo


def movie_crawl():
    base_url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = soup.select('#contents > div.wrap-movie-chart > div.sect-movie-chart')
    rank = []
    image = []
    title = []
    rate = []
    open_date = []
    url_number=[]

    for movie in movies:
        a_rank = movie.select('ol > li > div.box-image > strong')
        a_image = movie.select('ol > li > div.box-image > a > span > img')
        a_title = movie.select('ol > li > div.box-contents > a > strong')
        a_rate = movie.select('ol > li > div.box-contents > div > strong > span ')
        a_open_date = movie.select('ol > li > div.box-contents > span.txt-info > strong ')

        for i in range(0, len(a_rank)):
            rank.append(a_rank[i].getText())
            image.append(a_image[i]['src'])
            title.append(a_title[i].getText())
            rate.append(a_rate[i].getText())

            match_date = re.search(r'(\d{4}\.\d{2}\.\d{2})', a_open_date[i].getText())
            date_str = match_date.group(1).replace('.', '-') if match_date else None
            open_date.append(date_str)

            match = re.search(r'/(\d{5})/', a_image[i]['src'][::-1])  # Reversed string to match from the end
            url_number.append(match.group(1)[::-1] if match else None)

    movieinfo = []

    for i in range(0, len(title)):
        movie_data = {
            'img': image[i],
            'title': title[i],
            'opendate': open_date[i],
            'image_url': url_number[i],
        }
        movieinfo.append(movie_data)

# 저장
    for data in movieinfo:
        Movieinfo.objects.create(**data)

    







