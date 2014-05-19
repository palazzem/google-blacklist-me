from scrapy.contrib.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from ..utils.parser import urls_from_file
from ..items import CompanyItem


class SpiderBot(CrawlSpider):
    EMAIL_REGEX = "[a-zA-Z0-9.!#$%&'*+-/=?\^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*"
    name = 'bot'
    rules = (
        # Follow Google search links and parse like there's no tomorrow!
        Rule(SgmlLinkExtractor(restrict_xpaths=('//li//h3', )), process_links='filter_links', callback='parse_item'),
    )

    def filter_links(self, links):
        # Get only first 5 links if available
        return links[0:5]

    def __init__(self, filename=None, *args, **kwargs):
        super(SpiderBot, self).__init__(*args, **kwargs)

        # Get start urls from file
        self.start_urls = urls_from_file(filename) if filename else []

    def parse_item(self, response):
        selector = Selector(response)

        # Use regex to find valid emails
        emails = selector.re(self.EMAIL_REGEX)
        if (emails):
            item = CompanyItem({'link': response.url})
            item['emails'] = emails

            return item

        return
