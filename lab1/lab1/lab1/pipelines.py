# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter
from lxml import etree


class Lab1Pipeline:

    def __init__(self):
        self.root = etree.Element("data")

    def close_spider(self, spider):
        file = open('/home/supervisor/edu/database/lab1/results/isport_o.xml', 'wb')
        file.write(etree.tostring(
            self.root, encoding="UTF-8",
            pretty_print=True
        ))
        file.close()

    def process_item(self, item, spider):
        page = etree.SubElement(self.root, "page", url=item["url"])
        for text in item['texts']:
            etree.SubElement(page, 'fragment', type='text').text = text
        for image in item['images']:
            etree.SubElement(page, 'fragment', type='image').text = image
        self.root.append(page)
        return item
