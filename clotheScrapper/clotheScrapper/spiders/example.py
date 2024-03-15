import scrapy

class ClotheSpider(scrapy.Spider):
    name = "clothes"
    allowed_domains = ["aliexpress.com"]
    start_urls = ["https://aliexpress.com"]

    def parse(self, response):
        pass
