import scrapy


class VoucherCloudSpider(scrapy.Spider):
    name = 'vouchercloud_spider'
    start_urls = [ 

        'https://www.vouchercloud.com/asos-vouchers' ,	
        'https://www.vouchercloud.com/calvin-klein-collection-vouchers' ,
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.tile-list .tile-list-content .tile-list-title .hover-over'):
            item = {
                'vouchercloud': feed_item.css('::text').extract_first(),
            }
            yield item



