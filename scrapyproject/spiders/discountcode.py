import scrapy


class DiscountCodeSpider(scrapy.Spider):
    name = 'discountcode_spider'
    start_urls = [ 

        'https://discountcode.dailymail.co.uk/asos' ,	
        'https://discountcode.dailymail.co.uk/office-shoes' ,	
        'https://discountcode.dailymail.co.uk/schuh' ,	
        'https://discountcode.dailymail.co.uk/marks-and-spencer' ,	
        'https://discountcode.dailymail.co.uk/footasylum' ,	
        'https://discountcode.dailymail.co.uk/aldo' ,	
        'https://discountcode.dailymail.co.uk/boden' ,	
        'https://discountcode.dailymail.co.uk/joules' ,	
        'https://discountcode.dailymail.co.uk/stradivarius' ,	
        'https://discountcode.dailymail.co.uk/ted-baker' ,	
        'https://discountcode.dailymail.co.uk/geox' ,	
        'https://discountcode.dailymail.co.uk/kickers' ,	
        'https://discountcode.dailymail.co.uk/ecco' ,
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.deal .dailymailcouk-voucher-title-link'):
            item = {
                'DiscountCode': feed_item.css('::text').extract_first(),
            }
            yield item



