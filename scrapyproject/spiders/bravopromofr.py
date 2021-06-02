import scrapy


class BravopromoFrSpider(scrapy.Spider):
    name = 'bravopromo_fr_spider'
    start_urls = [ 

        'https://www.bravopromo.fr/code-promo-asos.html' ,
        'https://www.bravopromo.fr/code-promo-tailor-brands.html' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.merchant-deal__title'):
            item = {
                'BravopromoFr': feed_item.css('::text').extract_first(),
            }
            yield item



