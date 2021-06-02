import scrapy


class StudentBeansSpider(scrapy.Spider):
    name = 'studentbeans_spider'
    start_urls = [ 

        'https://www.studentbeans.com/student-discount/us/asos/0-student-discount-5be9308a-d64a-4680-8b28-42ac6c361fa3?source=quick_search' ,
        'https://www.studentbeans.com/student-discount/us/foot-locker/0-student-discount-daf52f04-ea6e-4bcd-8ca9-9404cee2dc65?source=recommended_search' ,	       
        
        ]
    
    def parse(self, response):
        for feed_item in response.css('._trxvlo ._1glzvfh'):
            item = {
                'StudentBeans': feed_item.css('::text').extract_first(),
            }
            yield item



