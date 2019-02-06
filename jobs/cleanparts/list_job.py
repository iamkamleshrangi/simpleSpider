from datetime import datetime
import copy, requests, sys
from lib.jobs_log import saveJob
from lib.common import getId, getguId 
from lib.rq_queue import getConnections
from bs4 import BeautifulSoup

jobs = {'is_crawled': 'False',
        'is_parsed': 'False',
        'storage_id': '',
        'extension':'htm',
        'insert_time': datetime.utcnow(),
        'update_time': datetime.utcnow(), 
        'crawl_queue': '', 
        'parse_queue': '',
        'domain': 'cleaningparts',
        'collection': 'cleaningparts',
        'job_script':'jobs.smchealth.list_jobs',
        'crawl_script': 'crawler.crawl.getPage',
        'parse_script':'parser.cleaningparts.list.parser', 
        'priorities': 'high',
        'storage_path': '',
        'crawl_count': 0 }

q = getConnections()
start_url =  'http://cleaningparts.pl/'
content = requests.get(start_url).content
soup = BeautifulSoup(content, 'html.parser')
job_arr = []
for record in soup.find_all("a", {"class":"main-cat"}):
    cat_url = record.get('href')
    cat_name = record.text
    content = requests.get(cat_url).content
    soup = BeautifulSoup(content, 'html.parser')
    soup = soup.find('div',{ 'class':'btns'})
    if soup:
        page_no = soup.find_all('a')[-1]
        page_nos = int(page_no.text)
        for page_no in range(1, page_nos + 1):
            sub_url = cat_url + 'p%s'%page_no
            msg = copy.deepcopy(jobs)
            msg['job_id'] = getguId()
            msg['input'] = {'url' : sub_url, 'category': cat_name}
            job_arr.append(msg)
    else:
        msg = copy.deepcopy(jobs)
        msg['job_id'] = getguId()
        msg['input'] = {'url' :cat_url, 'category':  cat_name}
        job_arr.append(msg)

for msg in job_arr:
    q.enqueue(msg['crawl_script'], msg)
    saveJob(msg)
