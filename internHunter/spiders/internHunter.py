import scrapy


class QuotesSpider(scrapy.Spider):
    name = "internshala"

    # def start_requests(self):
    #     urls = [
    #         'https://internshala.com/internships'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    # def start_requests(self):
    #     yield scrapy.Request(f'https://internshala.com/internships/keyword-{self.category}')   
    def __init__(self, category=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        print("cat:",category)
        self.start_urls = [f'https://internshala.com/internships/keywords-{category}']    

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'intern-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')