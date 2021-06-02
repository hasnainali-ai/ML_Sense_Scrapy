import scrapy


class DeIgraalSpider(scrapy.Spider):
    name = 'de_igraal_spider'
    start_urls = [ 

        'https://de.igraal.com/gutschein/ASOS' ,	
        'https://de.igraal.com/gutschein/calvin-klein' ,
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('div.voucher-detailed .voucher-detailed__inner .voucher-detailed__right .title '):
            item = {
                'DeIgraal': feed_item.css('::text').extract_first(),
            }
            yield item



