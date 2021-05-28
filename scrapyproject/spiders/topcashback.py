import scrapy


class TopCashbackSpider(scrapy.Spider):
    name = 'topcashback_spider'
    start_urls = [ 
        'https://www.topcashback.co.uk/clarks/' ,	
        'https://www.topcashback.co.uk/asos/' ,	
        'https://www.topcashback.co.uk/office-shoes/' ,	
        'https://www.topcashback.co.uk/schuh/' ,	
        'https://www.topcashback.co.uk/marks-and-spencer/' ,	
        'https://www.topcashback.co.uk/footasylum/' ,	
        'https://www.topcashback.co.uk/aldo/' ,	
        'https://www.topcashback.co.uk/boden/' ,	
        'https://www.topcashback.co.uk/joules-clothing/' ,	
        'https://www.topcashback.co.uk/stradivarius/' ,	
        'https://www.topcashback.co.uk/ted-baker/' ,	
        'https://www.topcashback.co.uk/geox-uk/' ,	
        'https://www.topcashback.co.uk/kickers/' ,
	
        ]
    
    def parse(self, response):
        for feed_item in response.css('.gecko-deeplink-title:nth-child(1)'):
            item = {
                'Title': feed_item.css('::text').extract_first(),
            }
            yield item



