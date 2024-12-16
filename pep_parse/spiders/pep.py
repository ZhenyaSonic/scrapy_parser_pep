import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for href in response.xpath(
            '//section[@id="numerical-index"]//table//tr//a/@href'
        ).getall():
            yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.xpath('//h1[@class="page-title"]/text()').get()
        number, name = title.split(' – ', 1)
        status = response.xpath('//abbr/text()').get()
        yield PepParseItem(
            status=status,
            name=name,
            number=number.replace('PEP ', ''),
        )
