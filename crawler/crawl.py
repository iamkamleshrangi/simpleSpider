import requests, os, uuid
from lib.config_handler import handler
from lib.jobs_log import updateJobStatus
from lib.common import getId
from lib.jobs_log import checkFile, samejobCount
from lib.rq_queue import getConnections

PATH = handler('settings','public_path')
def getPage(job):
    job_id = job['job_id']
    try:
        url = job['input']
        page = requests.get(url)
        if page.status_code == 200:
            html_content = page.content
            storage_id = getId(html_content)
            print(storage_id)
            status, storage_path = checkFile(storage_id)
            if status == False:
                file_path = savePage(html_content)
                job['storage_path'] = file_path
            elif status == True:
                job['storage_path'] = storage_path

            job['storage_id'] = storage_id
            job['is_crawled'] = "True"
            count = samejobCount(storage_id)
            job['crawl_count'] = count
            result = q.enqueue(msg['parse_script'], job)
            updateJobStatus(job_id, job)
        else:
            print('Already Crawled the page')
            return True
        return False
    except Exception as e:
        job['errors'] = e
        updateJobStatus(job_id, job)

def savePage(content):
    dir_path = PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = uuid.uuid4().hex + '.htm'
    file_path = dir_path + file_name
    with open(file_path, 'wb') as f:
        f.write(content)
    return file_path 
