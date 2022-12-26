import scrapy
from re import search
from urllib.parse import urlencode
from scrapy.item import Item, Field
from bestmovies.items import BestmoviesItem


API_KEY = '63c024e3-acf6-4fea-849c-a17d003e5d0b'

def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class FilmSpider(scrapy.Spider):
    name = 'kinopoisk'
    # start_urls = ['https://www.kinopoisk.ru/lists/movies/popular/']

    url = "https://www.kinopoisk.ru"

    def start_requests(self):
        start_url = 'https://www.kinopoisk.ru/lists/movies/popular/'
        yield scrapy.Request(url=get_proxy_url(start_url), callback=self.parse)

    def parse(self, response):
        film_item = BestmoviesItem()

        films = response.css('.styles_root__ti07r')


        for film in films:
            year_string = film.css('span.desktop-list-main-info_secondaryText__M_aus').get()
            try:
                year = search(r"(\d+)", year_string).group(1)
            except:
                print(year_string)
            film_item['rating'] = film.css('span.styles_position__TDe4E::text').get()
            film_item['name_russian'] = film.css('span.styles_mainTitle__IFQyZ.styles_activeMovieTittle__kJdJj::text').get()
            film_item['name_english'] = film.css('span.desktop-list-main-info_secondaryTitle__ighTt::text').get()
            film_item['year'] = year
            film_item['kinopoisk_rating'] = film.css('.styles_kinopoiskValueBlock__qhRaI span::text').get()
            yield film_item

        # next_page = response.css('.styles_root__AT6_5.styles_root__RoFSb a::attr(href)')[-1].get()
        #
        # if next_page is not None:
        #     next_page_url = self.url + next_page
        #     yield response.follow(get_proxy_url(next_page_url), callback=self.parse)