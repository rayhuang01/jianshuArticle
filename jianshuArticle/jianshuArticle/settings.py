# -*- coding: utf-8 -*-

# Scrapy settings for jianshuArticle project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jianshuArticle'

SPIDER_MODULES = ['jianshuArticle.spiders']
NEWSPIDER_MODULE = 'jianshuArticle.spiders'

FEED_URI='D:\Python\Scrapy\linkedin\linkedin\jianshu-hot.csv'
FEED_FORMAT='CSV'

DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'linkedin (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#  'Accept': '*/*',
#  'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
#  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#  'X-Requested-With': 'XMLHttpRequest',
#  'X-INFINITESCROLL':'true',
#  'Accept-Encoding':'gzip, deflate, br',
#  'Cache-Control':'no-cache',
#  'Connection':'keep-alive',
##  'Cookie':'read_mode=day; default_font=font2; sajssdk_2015_cross_new_user=1; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fc%2FJgq3Wc%3Forder_by%3Dadded_at%26page%3D1; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1514875541,1514877019,1514877108,1514877248; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1514882137; _ga=GA1.2.1213023521.1514866907; _gid=GA1.2.1176161623.1514866907; _gat=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22160b51a96abfd6-06fc5fe5df9d27-7b1f3c-2073600-160b51a96aca2c%22%2C%22%24device_id%22%3A%22160b51a96abfd6-06fc5fe5df9d27-7b1f3c-2073600-160b51a96aca2c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22not-signed-in-like-button%22%7D%2C%22first_id%22%3A%22%22%7D; locale=zh-CN; _m7e_session=2c198277b63c9da72a567e7602809728',
#  'Host':'www.jianshu.com',
#  'Pragma':'no-cache',
#  'Referer':'https://www.jianshu.com/c/Jgq3Wc?order_by=added_at&page=1',
#  'X-CSRF-Token':'+Aqgxl4XguWdw+DxqIKY0dmyU2gioJxFbFJgvejupXFmJGjm3RcyUO0fjUSonyjDoV859QOaJGf4QGUeXvA8nA=='
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jianshuArticle.middlewares.JianshuarticleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jianshuArticle.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jianshuArticle.pipelines.JianshuarticlePipeline': 300,
    'jianshuArticle.pipelines.MyImagePipeline': 1
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
FEED_EXPORTERS_BASE = {
    'json': 'scrapy.exporters.JsonItemExporter',
    'jsonlines': 'scrapy.exporters.JsonLinesItemExporter',
    'csv': 'scrapy.exporters.CsvItemExporter',
    'xml': 'scrapy.exporters.XmlItemExporter',
    'marshal': 'scrapy.exporters.MarshalItemExporter',
}
#FEED_FORMAT = "csv"
#FEED_URI = "feed_result/result_%(time)s.csv"
IMAGES_STORE = 'D:\\git\\zheyibu\\CrawlJianshuDoc-master\\jianshuArticle\\feed_result\\images'
IMAGES_THUMBS = {
    #'small': (50, 50),
    'big': (270, 270),
}