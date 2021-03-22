import scrapy
import logging


class ISportSpider(scrapy.Spider):
    name = 'isport'
    start_urls = ['https://isport.ua']
    selectors = {
        'text': '//*[not(self::script) and not(self::noscript) and not(self::style)]/text()[normalize-space()]',
        'image': '//img/@data-src',
        # 'url': "//a/@href[starts-with(., '" + start_urls[0] + "')or starts-with(., '/')]"
        'url': "//a/@href[starts-with(., '{}') or starts-with(., '/')]".format(start_urls[0])

    }

    def parse(self, response):
        yield {
            'url': response.url,
            'texts': response.xpath(self.selectors['text']).extract(),
            'images': response.xpath(self.selectors['image']).extract()
        }

        self.start_urls.append(response.url)

        if response.url == self.start_urls[0]:
            urls = response.xpath(self.selectors['url']).extract()
            for url in urls[:20]:
                if url != '/':
                    if url.startswith("/"):
                        url = self.start_urls[0] + url
                    yield response.follow(url, callback=self.parse)
