from datetime import datetime
import copy, requests, sys
from lib.jobs_log import saveJob
from lib.common import getId, getguId 
from lib.rq_queue import getConnections
from bs4 import BeautifulSoup
from lib.mongodb import operations

jobs = {'is_crawled': 'False',
        'is_parsed': 'False',
        'storage_id': '',
        'extension':'htm',
        'insert_time': datetime.utcnow(),
        'update_time': datetime.utcnow(), 
        'crawl_queue': '', 
        'parse_queue': '',
        'domain': 'cleaningparts',
        'collection': 'cleaningparts_parts',
        'job_script':'jobs.smchealth.jobs',
        'crawl_script': 'crawler.crawl.getPage',
        'parse_script':'parser.cleaningparts.parser.parser', 
        'priorities': 'high',
        'storage_path': '',
        'crawl_count': 0 }

q = getConnections()
start_url =  'http://cleaningparts.pl/'
records = operations().find_data('in', 'cleaningparts')
count = 1
for data_h in records:
    msg = copy.deepcopy(jobs)
    msg['input'] = {'url': data_h['part_url'], 'category': data_h['category'] }
    msg['job_id'] = getguId()
    print(msg)
    print('===')
    #q.enqueue(msg['crawl_script'], msg)
    #saveJob(msg)
