import requests #ADD PROXIES 
from lib.jobs_log import updateJobStatus, checkFile, samejobCount
from lib.common import getId, savePage
from lib.rq_queue import getConnections
from datetime import datetime

def getPage(job):
    job_id = job['job_id']
    q = getConnections()
    try:
        url = job['input']['url']
        page = requests.get(url)
        if page.status_code == 200:
            html_content = page.content
            storage_id = getId(html_content)
            status, storage_path = checkFile(storage_id)
            if status == False:
                file_path = savePage(html_content)
                job['storage_path'] = file_path
            elif status == True:
                job['storage_path'] = storage_path
            job['storage_id'] = storage_id
            job['is_crawled'] = "True"
            job['update_time'] = datetime.utcnow()
            count = samejobCount(storage_id)
            job['crawl_count'] = count
            print(job)
            #result = q.enqueue(job['parse_script'], job)
            #updateJobStatus(job_id, job)
        else:
            print('Already Crawled the page')
    except Exception as e:
        print(e)
        job['errors'] = e
        updateJobStatus(job_id, job)

job = {'is_crawled': 'False', 'is_parsed': 'False', 'storage_id': '', 'extension': 'htm',
        'insert_time': '', 'update_time': '', 'crawl_queue': '', 'parse_queue': '',
        'domain': 'cleaningparts', 'collection': 'cleaningparts_parts', 
        'job_script': 'jobs.smchealth.jobs', 'crawl_script': 'crawler.crawl.getPage',
        'parse_script': 'parser.cleaningparts.part.parser', 'priorities': 'high', 
        'storage_path': '', 'crawl_count': 0, 
        'input': {'url': 'http://cleaningparts.pl/szczotka-tt-ttb-345-p505', 'category': 'Wyprzedaż'},
        'job_id': 'bc42e76c51a14d548cef0e3525867725'}
getPage(job)
