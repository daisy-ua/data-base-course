import scrapy


class PortativSpider(scrapy.Spider):
    name = 'portativ'
    start_urls = ['https://portativ.ua/category_1648232.html?tip_telefona_fa14=179240']
    selectors = {
        'description': ".//div[@class='cataloggrid-item-name-block']/a[@title]/text()",
        'price': ".//span[@class='price-value UAH']/text()",
        'image': ".//img[@class='UI-CATALOG-PRODUCT-IMAGE']/@src"
    }

    def parse(self, response):
        products = response.xpath("//div[@class='port-i']")[:20]

        for product in products:
            yield {
                'description': product.xpath(self.selectors['description']).get().strip(),
                'price': product.xpath(self.selectors['price']).get().strip(),
                'image': product.xpath(self.selectors['image']).get().strip()
            }
