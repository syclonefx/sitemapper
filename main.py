from sitemapper.crawler import SiteMapper
from sitemapper.exporter import export_to_xml

if __name__ == "__main__":
    base = "https://syclonefx.com"
    spider = SiteMapper(base)
    spider.crawl(base)
    
    # Output plain sitemap
    for page in spider.get_sitemap():
        print(page)
    export_to_xml(spider.get_sitemap(), "sitemap.xml")