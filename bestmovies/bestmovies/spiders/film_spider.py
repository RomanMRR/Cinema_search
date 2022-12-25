import scrapy
from re import search


class FilmSpider(scrapy.Spider):
    name = 'kinopoisk'
    start_urls = ['https://www.kinopoisk.ru/lists/movies/popular/']
    COOKIES = {
        'location': '1',
        'ya_sess_id': '3:1671970572.5.0.1654788114563:lisdXg:2.1.2:1|449850237.4748981.2.2:4748981|1130000059033229.-1.0.2:1880687|30:10212606.72892.X63V8kVl5gL9EINWdPij4ufr6DI'
    }
    url = "https://www.kinopoisk.ru"

    def parse(self, response):
        films = response.css('.styles_root__ti07r')


        for film in films:
            year_string = film.css('span.desktop-list-main-info_secondaryText__M_aus').get()
            try:
                year = search(r"(\d+)", year_string).group(1)
            except:
                print(year_string)
            yield {
                'рейтинг': film.css('span.styles_position__TDe4E::text').get(),
                'название на русском': film.css('span.styles_mainTitle__IFQyZ.styles_activeMovieTittle__kJdJj::text').get(),
                'назвение на английском': film.css('span.desktop-list-main-info_secondaryTitle__ighTt::text').get(),
                'год выпуска': year,
                'рейтинг кинопоиска': film.css('.styles_kinopoiskValueBlock__qhRaI span::text').get()
            }

        next_page = response.css('.styles_root__AT6_5.styles_root__RoFSb a::attr(href)')[-1].get()

        if next_page is not None:
            next_page_url = self.url + next_page
            print(next_page_url)
            yield response.follow(next_page_url, callback=self.parse)
            # yield scrapy.Request(url=next_page_url, callback=self.parse, cookies=self.COOKIES)