import scrapy


class EasyFundraisingSpider(scrapy.Spider):
    name = 'easyfundraising_spider'
    start_urls = [ 

        'https://www.easyfundraising.org.uk/retailer/clarks/' ,	
        'https://www.easyfundraising.org.uk/retailer/asos/' ,	
        'https://www.easyfundraising.org.uk/retailer/office-shoes/' ,	
        'https://www.easyfundraising.org.uk/retailer/schuh' ,	
        'https://www.easyfundraising.org.uk/retailer/marks-and-spencer/' ,	
        'https://www.easyfundraising.org.uk/retailer/footasylum/' ,	
        'https://www.easyfundraising.org.uk/retailer/aldo/' ,	
        'https://www.easyfundraising.org.uk/retailer/boden/' ,	
        'https://www.easyfundraising.org.uk/retailer/joules/' ,	
        'https://www.easyfundraising.org.uk/retailer/stradivarius/' ,	
        'https://www.easyfundraising.org.uk/retailer/ted-baker/' ,	
        'https://www.easyfundraising.org.uk/retailer/geox/' ,	
        'https://www.easyfundraising.org.uk/retailer/kickers/' ,	
        'https://www.easyfundraising.org.uk/retailer/ecco-uk/' ,
	
        ]
    
    def parse(self, response):
        for feed_item in response.css('.mr__half p'):
            item = {
                'EasyFundraising': feed_item.css('::text').extract_first(),
            }
            yield item



