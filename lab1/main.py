from lxml import etree


def print_all_urls():
    root = etree.parse('results/isport.xml')
    urls = root.xpath('//page')
    for url in urls:
        print(f'{url.xpath("@url")[0]}')


def get_xhtml_page():
    transform = etree.XSLT(etree.parse('results/transformer.xsl'))
    result = transform(etree.parse('results/portativ.xml'))
    result.write('results/portativ.xhtml', pretty_print=True, encoding='UTF-8')


if __name__ == '__main__':
    print_all_urls()
    get_xhtml_page()
