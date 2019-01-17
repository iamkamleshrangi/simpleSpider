from redis import Redis
from rq import Queue
from crawler.crawl import getPage
import sys
q = Queue(connection=Redis())
start_url =  'https://www.goldeneagledirect.com/index.php?pg=%s&l=product_list&c=1'
page_starts_at = 1
page_ends_at = 16144

for i in range(page_starts_at, page_ends_at+1):
    page_url = start_url%(i)
    result = getPage(page_url)
    print(result)
    #result = q.enqueue(getPage, page_url)
    break
