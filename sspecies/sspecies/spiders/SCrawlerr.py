import codecs
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sspecies.items import SspeciesItem

class ScrawlerrSpider(CrawlSpider):
    name = "SCrawlerr"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Bird"]

    # rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)
    # Rule(LinkExtractor(allow=r'page/'), callback='parsepage', follow=True),
    # Rule(LinkExtractor(restrict_css='span.tag-item'), callback='parsepage', follow=True),
    # Rule(LinkExtractor(restrict_css='li.next'), callback='parsepage', follow=True),
    # Rule(LinkExtractor(allow=('/tag/'), deny=('.com/page/')), callback='parsepage', follow=True),

    def extractData(self, res):
        s = SspeciesItem()
        s['name'] = res.css('h1.firstHeading').css('span.mw-page-title-main::text').extract_first()
        s['bname'] = res.css('span.binomial').css('i::text').extract_first()
        self.writeTxt(s)

    def writeTxt(self, s):
        with codecs.open('data.txt', 'a+', 'utf-8') as f:
            f.write(s['name'] + '\r\n')
            f.write(s['bname'] + '\r\n')


def parsepage(self, res):
        self.extractData(res)

    # def parse_item(self, response):
    #     item = {}
    #     #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
    #     #item["name"] = response.xpath('//div[@id="name"]').get()
    #     #item["description"] = response.xpath('//div[@id="description"]').get()
    #     return item
