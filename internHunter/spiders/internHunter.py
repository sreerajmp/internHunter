import scrapy


class QuotesSpider(scrapy.Spider):
    name = "internshala"

    def start_requests(self):
        urls = [
            'https://internshala.com/internships'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'intern-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')