from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from bestmovies.spiders.film_spider import FilmSpider

process = CrawlerProcess(get_project_settings())
process.crawl(FilmSpider)
process.start()