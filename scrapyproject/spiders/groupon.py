import scrapy


class GrouponSpider(scrapy.Spider):
    name = 'groupon_spider'
    start_urls = [ 
        'https://www.groupon.co.uk/discount-codes/clarks' ,	
        'https://www.groupon.co.uk/discount-codes/asos' ,	
        'https://www.groupon.co.uk/discount-codes/office-shoes' ,	
        'https://www.groupon.co.uk/discount-codes/schuh' ,	
        'https://www.groupon.co.uk/discount-codes/marks-and-spencer' ,	
        'https://www.groupon.co.uk/discount-codes/footasylum' ,	
        'https://www.groupon.co.uk/discount-codes/aldo' ,	
        'https://www.groupon.co.uk/discount-codes/boden' ,	
        'https://www.groupon.co.uk/discount-codes/joules' ,	
        'https://www.groupon.co.uk/discount-codes/stradivarius' ,	
        'https://www.groupon.co.uk/discount-codes/ted-baker' ,
        'https://www.groupon.co.uk/discount-codes/kickers' ,	
        'https://www.groupon.co.uk/discount-codes/ecco' ,	
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.coupons-list-row .coupon-tile .coupon-tile-inner'):
            item = {
                'Title': feed_item.css('.coupon-tile-title::text').extract_first(),
            }
            yield item