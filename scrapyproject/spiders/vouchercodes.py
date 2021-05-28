import scrapy
# need proxy in this spider


class VoucherCodesSpider(scrapy.Spider):
    name = 'vouchercodes_spider'
    start_urls = [
        	
        'https://www.vouchercodes.co.uk/clarks.co.uk' ,	
        'https://www.vouchercodes.co.uk/asos.com' ,	
        'https://www.vouchercodes.co.uk/office.co.uk' ,	
        'https://www.vouchercodes.co.uk/schuhstore.co.uk' ,	
        'https://www.vouchercodes.co.uk/marksandspencer.com' ,	
        'https://www.vouchercodes.co.uk/footasylum.co.uk' ,	
        'https://www.vouchercodes.co.uk/aldoshoes.com' ,	
        'https://www.vouchercodes.co.uk/boden.co.uk' ,	
        'https://www.vouchercodes.co.uk/joulesclothing.com' ,
        'https://www.vouchercodes.co.uk/tedbaker.com' ,	
        'https://www.vouchercodes.co.uk/geox.com' ,	
        'https://www.vouchercodes.co.uk/kickers.co.uk' ,	
        'https://www.vouchercodes.co.uk/shopeu.ecco.com' ,
	
        ]
    
    def parse(self, response):
        for feed_item in response.css('div.feed .feed-item a'):
            item = {
                'Title': feed_item.css('span.card__title::text').extract_first(),
            }
            yield item



