import scrapy
#needs captcha


class MyVoucherCodesSpider(scrapy.Spider):
    name = 'myvouchercodes_spider'
    start_urls = [ 

        'https://www.myvouchercodes.co.uk/clarks' ,	
        'https://www.myvouchercodes.co.uk/asos' ,	
        'https://www.myvouchercodes.co.uk/office-shoes' ,	
        'https://www.myvouchercodes.co.uk/schuh' ,	
        'https://www.myvouchercodes.co.uk/marks-and-spencer' ,
        'https://www.myvouchercodes.co.uk/footasylum' ,	
        'https://www.myvouchercodes.co.uk/aldo' ,	
        'https://www.myvouchercodes.co.uk/boden-vouchers' ,	
        'https://www.myvouchercodes.co.uk/joules' ,	
        'https://www.myvouchercodes.co.uk/stradivarius' ,	
        'https://www.myvouchercodes.co.uk/ted-baker' ,	
        'https://www.myvouchercodes.co.uk/geox.com' ,	
        'https://www.myvouchercodes.co.uk/kickers' ,	
        'https://www.myvouchercodes.co.uk/ecco-shoes' ,	
	
        ]
    
    def parse(self, response):
        for feed_item in response.css(''):
            item = {
                'MyVoucherCodes': feed_item.css('::text').extract_first(),
            }
            yield item



