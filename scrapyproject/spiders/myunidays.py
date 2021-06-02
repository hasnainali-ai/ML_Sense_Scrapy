import scrapy


class MyunidaysSpider(scrapy.Spider):
    name = 'myunidays_spider'
    start_urls = [ 

        'https://www.myunidays.com/GB/en-GB/partners/asosclinique/view' ,
        'https://www.myunidays.com/GB/en-GB/partners/calvinklein/view' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('.benefit-body'):
            item = {
                'Myunidays': feed_item.css('::text').extract_first(),
            }
            yield item



