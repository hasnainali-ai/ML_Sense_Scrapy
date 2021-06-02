import scrapy


class GiveasyouliveSpider(scrapy.Spider):
    name = 'giveasyoulive_spider'
    
    start_urls = [ 

        'https://www.giveasyoulive.com/stores/asos' ,
        'https://www.giveasyoulive.com/stores/calvin-klein' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.order-md-1 .mt-2'):
            item = {
                'Giveasyoulive': feed_item.css('::text').extract_first(),
            }
            yield item



