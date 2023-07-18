import scrapy
import codecs

from sspecies.items import SspeciesItem

class SspiderSpider(scrapy.Spider):
    name = "SSpider"
    allowed_domains = ["wikipedia.org"]
    # start_urls = ["https://en.wikipedia.org/wiki/Bird"]
    start_urls = ["https://en.wikipedia.org/wiki/Great_crested_grebe"]

    def parse(self, response):
        self.extractData(response)


    def extractData(self, res):
        s = SspeciesItem()
        s['name'] = res.css('h1.firstHeading').css('span.mw-page-title-main::text').extract_first()
        self.writeTxt(s)

    def writeTxt(self, q):
        with codecs.open('data.txt', 'a+', 'utf-8') as f:
            f.write(q['name'] + '\r\n')

