import scrapy


class KortingscodeNlSpider(scrapy.Spider):
    name = 'kortingscode_nl_spider'
    start_urls = [ 

        'https://www.kortingscode.nl/asos' ,
        'https://www.kortingscode.nl/calvin-klein' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.kortingscodenl-voucher-title-link'):
            item = {
                'KortingscodeNl': feed_item.css('::text').extract_first(),
            }
            yield item



