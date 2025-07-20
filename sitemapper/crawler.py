import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

class SiteMapper:
    def __init__(self, base_url, delay=1):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.visited = set()
        self.delay = delay
        self.sitemap = []
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15"
            }

    def is_internal_link(self, url):
        return urlparse(url).netloc == self.domain or urlparse(url).netloc == ''

    def crawl(self, url):
        if url in self.visited:
            return
        self.visited.add(url)

        try:
            response = requests.get(url, headers=self.headers, timeout=5)
            if response.status_code != 200 or 'text/html' not in response.headers.get('Content-Type', ''):
                return
        except requests.RequestException:
            return

        print(f"Crawling: {url}")
        self.sitemap.append(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)

        for link in links:
            href = link['href'].split('#')[0]
            next_url = urljoin(url, href)
            if self.is_internal_link(next_url):
                self.crawl(next_url)
        
        time.sleep(self.delay)

    def get_sitemap(self):
        return self.sitemap