import scrapy


class QuidcoSpider(scrapy.Spider):
    name = 'quidco_spider'
    start_urls = [ 

        'https://www.quidco.com/clarks/' ,	
        'https://www.quidco.com/asos/' ,	
        'https://www.quidco.com/office-shoes/' ,	
        'https://www.quidco.com/schuh/' ,	
        'https://www.quidco.com/marks-spencer/' ,	
        'https://www.quidco.com/footasylum' ,	
        'https://www.quidco.com/aldo-shoes' ,	
        'https://www.quidco.com/boden/' ,	
        'https://www.quidco.com/joules' ,	
        'https://www.quidco.com/stradivarius/' ,	
        'https://www.quidco.com/ted-baker' ,	
        'https://www.quidco.com/geox' ,	
        'https://www.quidco.com/kickers' ,
	
        ]
    
    def parse(self, response):
        for feed_item in response.css('.pr-6 > .mb-3'):
            item = {
                'Title': feed_item.css('::text').extract_first(),
            }
            yield item



