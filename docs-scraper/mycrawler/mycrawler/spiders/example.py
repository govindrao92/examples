import scrapy

from scrapy.spiders import SitemapSpider


class MySpider(SitemapSpider):
    name = "example"
    allowed_domains = ["clickhouse.com"]

    sitemap_urls = ["https://clickhouse.com/docs/sitemap.xml"]

    def parse(self, response):
        pass  # ... scrape item here ...
