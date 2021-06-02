import scrapy


class BravoscontoItSpider(scrapy.Spider):
    name = 'bravosconto_it_spider'
    start_urls = [ 

        'https://www.bravosconto.it/codice-sconto-asos.html' ,
        'https://www.bravosconto.it/codice-sconto-tommy-hilfiger.html' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.iubenda-cs-btn-primary , .merchant-deal__title'):
            item = {
                'BravoscontoIt': feed_item.css('::text').extract_first(),
            }
            yield item



