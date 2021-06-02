import scrapy


class WidiloEsSpider(scrapy.Spider):
    name = 'widilo_es_spider'
    start_urls = [ 

        'https://www.widilo.es/codigo-descuento/asos' ,	
        'https://www.widilo.es/codigo-descuento/calvin-klein' ,
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.widilo-coupon-title'):
            item = {
                'WidiloEs': feed_item.css('::text').extract_first(),
            }
            yield item



