import scrapy


class DiscountVouchersSpider(scrapy.Spider):
    name = 'discountvouchers_spider'
    start_urls = [ 

        'https://www.discountvouchers.co.uk/clarks/' ,	
        'https://www.discountvouchers.co.uk/asos/' ,	
        'https://www.discountvouchers.co.uk/officeshoes/' ,	
        'https://www.discountvouchers.co.uk/schuh/' ,	
        'https://www.discountvouchers.co.uk/3837.html' ,	
        'https://www.discountvouchers.co.uk/footasylum/' ,	
        'https://www.discountvouchers.co.uk/aldo/' ,	
        'https://www.discountvouchers.co.uk/boden/' ,	
        'https://www.discountvouchers.co.uk/joulesclothing/' ,
        'https://www.discountvouchers.co.uk/tedbaker/' ,
        'https://www.discountvouchers.co.uk/kickers/' ,	
        'https://www.discountvouchers.co.uk/ecco-shoes-uk/' ,
        'https://www.discountvouchers.co.uk/tommyhilfiger/' ,	
	
        ]
    
    def parse(self, response):
        for feed_item in response.css('.dv-merchant-deals ul.deals li .voucher-details h3 a'):
            item = {
                'Title': feed_item.css('::attr(title)').extract_first(),
            }
            yield item



