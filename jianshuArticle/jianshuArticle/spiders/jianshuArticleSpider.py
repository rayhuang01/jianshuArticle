import scrapy
import json
from datetime import datetime
from scrapy.selector import Selector
from urllib import parse
#import pymongo
from jianshuArticle.items import JianshuarticleItem, ArticleReviewItem
#from selenium import webdriver
#from scrapy.http import TextResponse
#from scrapy.selector import HtmlXPathSelector
#from laptop_sample.items import LaptopSampleItem

class jianshuArticleSpider(scrapy.spiders.Spider):
    
    name = "jianshuArticle"
    allowed_domains = ["jianshu.com"]
    start_urls = []
    custom_settings={
            'MONGO_URI':'mongodb://192.168.8.119:2222/',
            'MONGO_DATEBASE':'zheyibu'
            }
        
    for i in range(1,202):
        start_urls.append('https://www.jianshu.com/c/Jgq3Wc?order_by=added_at&page={}'.format(i))
#    print(start_urls)
    
    def parse(self, response):
        if response.status == 200:
            selector = Selector(response)
            articles = selector.xpath('//ul[@class="note-list"]/li').extract()
            for obj in articles:
                sel = Selector(text=obj, type="html")

                articleid = sel.xpath('//li/@data-note-id')[0].extract()
                url = "http://www.jianshu.com" + sel.xpath('//a[@class="title"]/@href')[0].extract()
                
                yield scrapy.Request(url=url,callback=self.parse_article,meta={'articleid':articleid})
        else:
            print ('search failed: %s',response.url)
            
    def parse_article(self, response):
        if response.status == 200:
            articleid = response.meta.get('articleid')
            content = parse.unquote(response.selector.xpath('//div[@class="article"]/div[@class="show-content"]').extract_first())
            content = content.replace("data-original-src","src",10)
            datetimestr = response.xpath('//div[@class="article"]/div[@class="author"]/div[@class="info"]/div[@class="meta"]/span[@class="publish-time"]/text()').extract_first().strip('\n')
#            datetime_object = datetime.strptime(datetimestr, '%b %d %Y %I:%M%p')
            date = datetimestr.split(' ')[0].replace('.','-')
            author = response.xpath('//div[@class="article"]/div[@class="author"]/div[@class="info"]/span[@class="name"]/a/text()').extract_first()
            
            item = JianshuarticleItem()
            item['reviewurl'] = response.url
            item['articleId'] = articleid
            item['content'] = content
            item['author'] = author
            item['date'] = date
            item['title'] = response.selector.xpath('//div[@class="article"]/h1[@class="title"]/text()').extract_first()
            item['image_urls'] = [parse.unquote(src) for src in response.xpath('//div[@class="article"]//img/@data-original-src').extract()]

            yield item
            
            headers = {
               'cache-control':'no-cache',
               'Accept':'*/*',
               'Host':'www.jianshu.com',
               'Content-Type'	:'application/x-www-form-urlencoded; charset=UTF-8',
               'Origin':'http://jianlika.com',
               'Accept-Encoding':'gzip, deflate, br',
               'Accept-Language':'zh-CN,zh;q=0.9',
               'Connection':'keep-alive',
               'Cookie':'_ga=GA1.2.1213023521.1514866907; _gid=GA1.2.1176161623.1514866907; read_mode=day; default_font=font2; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fp%2F27de765cdb28; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1514877108,1514877248,1514889500,1514940216; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1514944499; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22160b51a96abfd6-06fc5fe5df9d27-7b1f3c-2073600-160b51a96aca2c%22%2C%22%24device_id%22%3A%22160b51a96abfd6-06fc5fe5df9d27-7b1f3c-2073600-160b51a96aca2c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22not-signed-in-like-button%22%7D%2C%22first_id%22%3A%22%22%7D; locale=zh-CN; _m7e_session=379b69321bf134c96d22b08badcfd63b',
               'Pragma':'no-cache',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
               }
            
            headers['Referer'] = response.url
            # process comments for first page here
            commenturl = "https://www.jianshu.com/notes/" + articleid + "/comments?comment_id=&author_only=false&since_id=0&max_id=1586510606000&order_by=likes_count&page=1"
            yield scrapy.Request(url=commenturl,headers=headers,callback=self.parse_comment,meta={'articleid':articleid,'headers':headers})
            
        else:
            print ('search failed: %s',response.url)
            
    def parse_comment(self, response):
        if response.status == 200:
            jsonobject = json.loads(response.text)
            
            page = jsonobject['page']
            total_pages = jsonobject['total_pages']
            comments = jsonobject['comments']
            
            articleid = response.meta.get('articleid')
            
            for comment in comments:
                if(comment):
                    review = comment['compiled_content']
                    commentdatestr = comment['created_at']
#                    datetime_object = datetime.strptime(commentdatestr, '%b %d %Y %I:%M%p')
                    commentdate = commentdatestr.split('T')[0].replace('.','-')
                    reviewid = str(comment['id'])
                    
                    user = comment['user']
                    if user:
                        username = user['nickname']
                        
                        com = ArticleReviewItem()
                        com['user'] = username
                        com['date'] = commentdate
                        com['review'] = review
                        com['articleId'] = articleid
                        com['reviewId'] = reviewid
                        
                        yield com
                    
                    # child comments
                    childs = comment['children']
                    
                    if childs:
                        for child in childs:
                            if child:
                                child_review = child['compiled_content']
                                child_commentdatestr = child['created_at']
#                                child_datetime_object = datetime.strptime(child_commentdatestr, '%b %d %Y %I:%M%p')
                                child_commentdate = child_commentdatestr.split('T')[0].replace('.','-')
                                child_reviewid = str(child['id'])
                                
                                child_user = child['user']
                                if child_user:
                                    child_username = child_user['nickname']
                                    
                                    child_com = ArticleReviewItem()
                                    child_com['user'] = child_username
                                    child_com['date'] = child_commentdate
                                    child_com['review'] = child_review
                                    child_com['articleId'] = articleid
                                    child_com['reviewId'] = child_reviewid
                                    
                                    yield child_com
                        
            headers = response.meta.get('headers')
            
            if total_pages > page:
                # process comments
                commenturl = ("https://www.jianshu.com/notes/" + articleid + "/comments?comment_id=&author_only=false&since_id=0&max_id=1586510606000&order_by=likes_count&page={}").format(page + 1)
                yield scrapy.Request(url=commenturl,headers=headers,callback=self.parse_comment,meta={'articleid':articleid})
                        
        else:
            print ('search failed: %s',response.url)
            
            
            
            
            
            