import scrapy



class ActiesNlSpider(scrapy.Spider):
    name = 'acties_nl_spider'
    start_urls = [ 

        'https://www.acties.nl/asos' ,	
        'https://www.acties.nl/calvin-klein' ,
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.font-icon h3'):
            item = {
                'ActiesNl': feed_item.css('::text').extract_first(),
            }
            yield item



