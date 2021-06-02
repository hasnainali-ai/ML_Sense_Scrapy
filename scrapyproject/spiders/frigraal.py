import scrapy


class FrIgraalSpider(scrapy.Spider):
    name = 'fr_igraal_spider'
    start_urls = [ 

        'https://fr.igraal.com/codes-promo/ASOS' ,
        'https://fr.igraal.com/codes-promo/calvin-klein' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('div.voucher-detailed .voucher-detailed__inner .voucher-detailed__right .title '):
            item = {
                'FrIgraal': feed_item.css('::text').extract_first(),
            }
            yield item



