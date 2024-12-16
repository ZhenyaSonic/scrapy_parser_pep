import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{allowed_domains[0]}/']

    def parse(self, response):
        pep_links = response.xpath(
            '//section[@id="numerical-index"]//table//tr//a/@href'
        ).getall()
        for href in pep_links:
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
