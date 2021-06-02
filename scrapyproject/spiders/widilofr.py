import scrapy


class WidiloFrSpider(scrapy.Spider):
    name = 'widilo_fr_spider'
    start_urls = [ 

        'https://www.widilo.fr/code-promo/asos' ,	
        'https://www.widilo.fr/code-promo/calvin-klein' ,
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.widilo-coupon-title'):
            item = {
                'WidiloFr': feed_item.css('::text').extract_first(),
            }
            yield item



