import scrapy


class GlamourrewardsSpider(scrapy.Spider):
    name = 'Glamourrewards_spider'
    
    start_urls = [ 

        'https://www.glamourrewards.com/me____.htm?keywords=ASOS.com&gmid=3069' ,
        'https://www.glamourrewards.com/me____.htm?keywords=Calvin%20Klein&gmid=3077' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.mn_description .mn_descriptionText'):
            item = {
                'Glamourrewards': feed_item.css('::text').extract_first(),
            }
            yield item



