from redis import Redis
from rq import Queue
from crawler.crawl import getPage
import sys
from datetime import datetime
import copy
from lib.jobs_log import saveJob

q = Queue(connection=Redis())
start_url =  'https://www.goldeneagledirect.com/index.php?pg=%s&l=product_list&c=1'
page_starts_at = 1
page_ends_at = 16144

jobs = {'is_crawled': 'False',
        'is_parsed': 'False',
        'storage_id': '',
        'extension':'htm',
        'insert_time': datetime.utcnow(),
        'update_time': datetime.utcnow(), 
        'crawl_queue': '', 
        'parse_queue': '',
        'job_script':'',
        'parse_script':'', 
        'priorities': 'high'}

for i in range(page_starts_at, page_ends_at+1):
    page_url = start_url%(i)
    msg = copy.deepcopy(jobs)
    msg['input'] = page_url
    result = q.enqueue(getPage, page_url)
    saveJob(msg)
