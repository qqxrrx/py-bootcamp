# https://books.toscrape.com

import scrapy


class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css('.price_color::text').extract_first(),
                'title': article.css('h3 > a::attr(title)').extract_first(),
            }
            next = response.css('.next > a::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)


# >>> py -m pip install scrapy

# use csv file extension to create a valid .csv file
# >>> scrapy runspider -o books.csv scrapy_book.py

# change file extension and it will create a valid .json file
# >>> scrapy runspider -o books.json scrapy_book.py
