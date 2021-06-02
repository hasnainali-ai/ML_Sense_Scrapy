import scrapy


class SparweltDeSpider(scrapy.Spider):
    name = 'sparwelt_de_spider'
    start_urls = [ 

        'https://www.sparwelt.de/gutscheine/asos' ,	
        'https://www.sparwelt.de/gutscheine/calvin-klein' ,
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.ui-teaser-info__heading'):
            item = {
                'SparweltDe': feed_item.css('::text').extract_first(),
            }
            yield item



