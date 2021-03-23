from lxml import etree


class Lab1Pipeline:

    def __init__(self):
        self.root = etree.Element("data")

    def close_spider(self, spider):
        with open('../../../results/%s.xml' % spider.name, 'wb') as file:
            file.write(etree.tostring(self.root, encoding="UTF-8", pretty_print=True, xml_declaration=True))
        file.close()

    def process_item(self, item, spider):
        if spider.name == 'isport':
            page = etree.SubElement(self.root, "page", url=item["url"])
            for text in item['texts']:
                etree.SubElement(page, 'fragment', type='text').text = text.strip()
            for image in item['images']:
                etree.SubElement(page, 'fragment', type='image').text = image
            self.root.append(page)
        else:
            product = etree.SubElement(self.root, "product")
            etree.SubElement(product, 'description', type='text').text = item['description']
            etree.SubElement(product, 'price', type='text').text = item['price']
            etree.SubElement(product, 'image', type='image').text = item['image']
            self.root.append(product)
        return item
