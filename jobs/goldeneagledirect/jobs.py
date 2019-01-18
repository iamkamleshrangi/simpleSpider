from redis import Redis
from rq import Queue
import sys
from datetime import datetime
import copy
from lib.jobs_log import saveJob
from lib.common import getId, getguId 

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
        'job_script':'jobs.goldeneagledirect.jobs',
        'crawl_script': 'crawler.crawl.getPage',
        'parse_script':'parser.goldeneagledirect.parser', 
        'priorities': 'high',
        'storage_path': '',
        'crawl_count': 0 }

count = 1
for i in range(page_starts_at, page_ends_at+1):
    page_url = start_url%(i)
    page_url = 'https://www.goldeneagledirect.com/index.php?pg=15&l=product_list&c=1'
    msg = copy.deepcopy(jobs)
    msg['input'] = page_url
    msg['job_id'] = getguId()
    result = q.enqueue(msg['crawl_script'], msg)
    saveJob(msg)
    if count == 10:
        break
    count += 1
    #break
