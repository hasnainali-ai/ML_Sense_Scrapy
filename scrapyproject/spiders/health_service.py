import scrapy


class HealthServiceSpider(scrapy.Spider):
    name = 'healthservice_spider'
    start_urls = [ 
        'https://healthservicediscounts.com/retailers/clarks-1266' ,
        'https://healthservicediscounts.com/retailers/asos-1711' ,
        'https://healthservicediscounts.com/retailers/office-1885' ,
        'https://healthservicediscounts.com/retailers/schuh-2246' ,
        'https://healthservicediscounts.com/retailers/ms-1498' ,
        'https://healthservicediscounts.com/retailers/footasylum-1078' ,
        'https://healthservicediscounts.com/retailers/boden-485' ,
        'https://healthservicediscounts.com/retailers/joules-1817' ,
        'https://healthservicediscounts.com/retailers/ted-baker-1021' ,
        'https://healthservicediscounts.com/retailers/kickers-634' ,
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('div.feed .feed-item a'):
            item = {
                'HealthService': feed_item.css('span.card__title::text').extract_first(),
            }
            yield item



