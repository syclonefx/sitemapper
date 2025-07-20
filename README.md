# SiteMapper

A Python-based site crawler that generates a sitemap of internal links. A sitemap.xml file is exported to the current working directory.

## Requirements
- Python 3.8+
- BeautifulSoup4 - [https://pypi.org/project/beautifulsoup4/](https://pypi.org/project/beautifulsoup4/)   
`https://pypi.org/project/beautifulsoup4/`
- requests - [https://pypi.org/project/requests/](https://pypi.org/project/requests/)   
`pip install requests`

**Install the required requirements**   
`pip install -r requirements.txt`

**Run sitemapper**   
`python main.py`

### Project Structure
sitemapper/   
│   
├── sitemapper/   
│   ├── __init__.py   
│   ├── crawler.py   
│   ├── exporter.py   
│   
└── main.py   

