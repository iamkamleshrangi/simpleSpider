from bs4 import BeautifulSoup as bs
from lib.common import getContent
from lib.mongodb import operations
from lib.jobs_log import updateJobStatus
import re, datatime

def parser(job):
    obj = operations()
    job_id = job['job_id']
    file_path = job['storage_path']
    list_url = job['input']['url']
    category = job['input']['category']
    content = getContent(file_path)
    soup = bs(content, 'html.parser')
    for part_url in soup.find_all('h3',{"class":"product-name"}):
        part_url = part_url.a.get('href')
        data = {'part_url': part_url, 
                'job_id': job_id, 
                'domain': 'cleanparts',
                'category': category }
        obj.insert_one('in', job['collection'], data)
    #Log to database
    obj.closeConnection()
    job['update_time'] = datetime.utcnow()
    job['is_parsed'] = "True"
    updateJobStatus(job['job_id'], job)
