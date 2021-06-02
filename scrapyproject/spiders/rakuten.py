import scrapy


class RakutenSpider(scrapy.Spider):
    name = 'rakuten_spider'
    
    start_urls = [ 

        'https://www.rakuten.com/asos.com' ,
        'https://www.rakuten.com/calvinklein.com' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.title-part'):
            item = {
                'Rakuten': feed_item.css('::text').extract_first(),
            }
            yield item



