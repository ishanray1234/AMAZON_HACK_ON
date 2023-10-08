import scrapy
from scrapy import Request
from fake_useragent import UserAgent


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=electronics/"]

    def start_requests(self):
        ua = UserAgent()
        user_agent = ua.random

        headers = {
            'Connection': 'keep-alive',
            'rtt': '300',
            'downlink': '0.4',
            'ect': '3g',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'en-US,en;q=0.9,ko;q=0.8',
        }
        yield Request(url=self.start_urls[0], headers=headers, callback=self.parse)

    def parse(self, response):
        filter_names = response.xpath(
            '//div[contains(@class, "a-section")]').getall()

        print("What I get ", filter_names)
        # Save the filter names to a file
        with open('filters.txt', 'w', encoding='utf-8') as file:
            for filter_name in filter_names:
                file.write(filter_name.strip() + '\n')

        # self.log('Filters saved to filters.txt')
        # with open('amazon_html.html', 'w', encoding='utf-8') as file:
        #     file.write(response.text)

        # self.log('HTML document saved to amazon_html.html')
