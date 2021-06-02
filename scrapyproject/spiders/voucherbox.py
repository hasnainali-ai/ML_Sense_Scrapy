import scrapy


class VoucherBoxSpider(scrapy.Spider):
    name = 'voucherbox_spider'
    start_urls = [ 

        'https://www.voucherbox.co.uk/vouchers/clarks' ,	
        'https://www.voucherbox.co.uk/vouchers/asos' ,	
        'https://www.voucherbox.co.uk/vouchers/office-shoes' ,	
        'https://www.voucherbox.co.uk/vouchers/schuh' ,	
        'https://www.voucherbox.co.uk/vouchers/marks-and-spencer' ,	
        'https://www.voucherbox.co.uk/vouchers/footasylum' ,	
        'https://www.voucherbox.co.uk/vouchers/aldo' ,	
        'https://www.voucherbox.co.uk/vouchers/boden' ,	
        'https://www.voucherbox.co.uk/vouchers/joules' ,	
        'https://www.voucherbox.co.uk/vouchers/stradivarius' ,	
        'https://www.voucherbox.co.uk/vouchers/ted-baker' ,	
        'https://www.voucherbox.co.uk/vouchers/geox' ,	
        'https://www.voucherbox.co.uk/vouchers/kickers' ,	
        'https://www.voucherbox.co.uk/vouchers/ecco' ,
	
        ]
    
    def parse(self, response):
        for feed_item in response.css(''):
            item = {
                'VoucherBox': feed_item.css('::text').extract_first(),
            }
            yield item



