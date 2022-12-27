# Kinopoisk parser

🔥 Парсер для получения информации о 1000 самых популярных фильмах 🔥

Считываются следующий данные


| Номер в рейтинге | Название на русском | Название на английском | Год выпуска | Рейтинг кинопоиска |
|------------------|---------------------|------------------------|-------------|--------------------|

Парсер реализован с использованием фреймворка **Scrapy**

Одной из основных проблем при считывании данных была блокировка от кинопоиска, который постоянно выдавал проверку на робота.
Для решения этой проблемы я воспользовался пакетом **scrapy-user-agents**, который автоматически меняет User-Agent. А также
прокси-сервисами от [ScrapeOps](https://scrapeops.io/proxy-aggregator/).

В файле film.csv содержатся полученные данные с использованием реализованного парсера.

## Инструкция для запуска
### Запуск скрипта


Для запуска скрипта у себя на компьютере проделайте следующее:
Скопируйте данный репозиторий 
```
git clone https://github.com/RomanMRR/Cinema_search.git
```
Перейдите в папку проекта
```
cd Cinema_search/bestmovies/
```
Установите необходимые пакеты
```
pip install -r requirements.txt
```
Запустите скрипт
```
python go-spider.py
```

Полученные данные будут сохранены в файле csv в папке `Cinema_search/bestmovies/data`

### Запуск с использованием Docker
Скопируйте данный репозиторий 
```
git clone https://github.com/RomanMRR/Cinema_search.git
```
Перейдите в папку проекта
```
cd Cinema_search/bestmovies/
```
Запустите
```
docker-compose up 
```
Чтобы получить файл с данными о фильмах выполните
```
docker cp bestmovies:/usr/src/app/data .
```
Нужный csv файл будет в папке data

### Сменя прокси-сервера

Если вы хотите использовать свой прокси-сервер, то можно изменить его API ключ в файле `Cinema_search/bestmovies/bestmovies/.env`. А также переопределить его работу в функцие `get_proxy_url` в файле `Сinema_search\bestmovies\bestmovies\spiders\film_spider.py`.

Если вы хотите также использовать ScrapeOps, но только со своим API ключом, тогда только пропишите свой API ключ в файле `Cinema_search/bestmovies/bestmovies/.env`.











