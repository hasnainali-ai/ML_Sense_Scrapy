import scrapy


class PromotionalCodesSpider(scrapy.Spider):
    name = 'promotionalcodes_spider'
    
    start_urls = [ 

        'https://www.promotionalcodes.org.uk/asos/' ,
        'https://www.promotionalcodes.org.uk/tommy-hilfiger/' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('h3 a'):
            item = {
                'PromotionalCodes': feed_item.css('::text').extract_first(),
            }
            yield item



