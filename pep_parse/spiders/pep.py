import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep_link in response.css(
            'section[id=numerical-index] tbody a::attr(href)'
        ):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().split()
        name = ' '.join(title[3:])
        yield PepParseItem({
            'number': int(title[1]),
            'name': name,
            'status': response.css('dt:contains("Status") + dd::text').get()
        })
