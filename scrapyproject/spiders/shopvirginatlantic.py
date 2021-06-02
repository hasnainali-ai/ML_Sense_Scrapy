import scrapy


class ShopVirginAtlanticSpider(scrapy.Spider):
    name = 'shopvirginatlantic_spider'
    
    start_urls = [ 

        'https://shop.virgin-atlantic.com/en/clothes-and-fashion/asos-uk' ,
        'https://shop.virgin-atlantic.com/en/clothes-and-fashion/calvin-klein-uk' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('#merchant-single .merch-rates'):
            item = {
                'ShopVirginAtlantic': feed_item.css('::text').extract_first(),
            }
            yield item



