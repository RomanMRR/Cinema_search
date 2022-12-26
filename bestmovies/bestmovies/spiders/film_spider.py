import os

import scrapy
from re import search
from urllib.parse import urlencode
from bestmovies.items import BestmoviesItem
from dotenv import load_dotenv, find_dotenv
import logging

load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")

API_KEY = os.getenv('API_KEY')


def get_year(year_string, film_name):
    try:
        year = search(r"(\d+)", year_string).group(1)
        return year
    except:
        logging.error(f"Ошибка при получении года в фильме {film_name}")
        return ""


def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class FilmSpider(scrapy.Spider):
    name = 'kinopoisk'
    start_url = 'https://www.kinopoisk.ru/lists/movies/popular/'
    main_url = "https://www.kinopoisk.ru"

    def start_requests(self):

        yield scrapy.Request(url=get_proxy_url(self.start_url), callback=self.parse)

    def parse(self, response):
        film_item = BestmoviesItem()

        films = response.css('.styles_root__ti07r')

        for film in films:
            film_item['rating'] = film.css('span.styles_position__TDe4E::text').get()
            film_item['name_russian'] = film.css(
                'span.styles_mainTitle__IFQyZ.styles_activeMovieTittle__kJdJj::text').get()
            film_item['name_english'] = film.css('span.desktop-list-main-info_secondaryTitle__ighTt::text').get()
            year_string = film.css('span.desktop-list-main-info_secondaryText__M_aus').get()
            year = get_year(year_string, film_item['name_russian'])
            film_item['year'] = year
            film_item['kinopoisk_rating'] = film.css('.styles_kinopoiskValueBlock__qhRaI span::text').get()
            yield film_item

        next_page = response.css('.styles_root__AT6_5.styles_root__RoFSb a::attr(href)')[-1].get()

        if next_page is not None:
            next_page_url = self.main_url + next_page
            yield response.follow(get_proxy_url(next_page_url), callback=self.parse)
