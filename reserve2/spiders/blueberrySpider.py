import scrapy

class blueberrySpider(scrapy.Spider):
    name = 'blueberry'
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        for article in response.css('.athing'):
            yield{
                'id': article.css('tr ::attr(id)').get(),
                'title': article.css('td.title > a ::text').get(),
                'link': article.css('td.title > a ::attr(href)').get(),
                'point': article.xpath('following-sibling::*').css('td.subtext > span ::text').get()
              }

        ## for next_page in response.css('a.morelink'):
        ##    yield response.follow(next_page, self.parse)