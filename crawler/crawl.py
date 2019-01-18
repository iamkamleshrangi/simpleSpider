import requests, os, uuid
from lib.config_handler import handler
from lib.jobs_log import updateJobStatus
from lib.common import getId

PATH = handler('settings','public_path')
def getPage(job):
    url = job['input']
    job_id = job['job_id']
    page = requests.get(url)
    if page.status_code == 200:
        html_content = page.content
        file_path = savePage(html_content)
        job['storage_path'] = file_path
        job['is_crawled'] = "True"
        job['storage_id'] = getId(html_content)
        updateJobStatus(job_id, job)
        return True
    return False

def savePage(content):
    dir_path = PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = uuid.uuid4().hex + '.htm'
    file_path = dir_path + file_name
    with open(file_path, 'wb') as f:
        f.write(content)
    return file_path 
