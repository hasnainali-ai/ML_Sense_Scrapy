import scrapy


class KidstartSpider(scrapy.Spider):
    name = 'kidstart_spider'
    
    start_urls = [ 

        'https://www.kidstart.co.uk/partner/ASOS.aspx' ,
        'https://www.kidstart.co.uk/partner/JohnLewis.aspx' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.percent-saving'):
            item = {
                'Kidstart': feed_item.css('::text').extract_first(),
            }
            yield item



