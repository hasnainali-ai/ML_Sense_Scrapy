import scrapy


class ThegivingmachineSpider(scrapy.Spider):
    name = 'thegivingmachine_spider'
    
    start_urls = [ 

        'https://www.thegivingmachine.co.uk/shop/asos' ,
        'https://www.thegivingmachine.co.uk/shop/john-lewis-and-partners' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.right'):
            item = {
                'Thegivingmachine': feed_item.css('::text').extract_first(),
            }
            yield item



