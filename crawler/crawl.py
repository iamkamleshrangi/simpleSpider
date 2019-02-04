import requests
from lib.jobs_log import updateJobStatus, checkFile, samejobCount
from lib.common import getId, savePage
from lib.rq_queue import getConnections

def getPage(job):
    job_id = job['job_id']
    q = getConnections()
    try:
        url = job['input']
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

            count = samejobCount(storage_id)
            job['crawl_count'] = count
            result = q.enqueue(job['parse_script'], job)
            updateJobStatus(job_id, job)
        else:
            print('Already Crawled the page')
    except Exception as e:
        print(e)
        job['errors'] = e
        updateJobStatus(job_id, job)

job = {'is_crawled': 'True', 'is_parsed': 'False', 'storage_id': 'a265c56d93ef498f2cf6685162bbb993',
        'extension': 'htm', 'insert_time': '', 'update_time': '', 'crawl_queue': '', 'parse_queue': '',
        'domain': 'smchealth', 'job_script': 'jobs.smchealth.jobs', 'crawl_script': 'crawler.crawl.getPage',
        'parse_script': 'parser.smchealth.parser.run', 'priorities': 'high',
        'storage_path': '/Users/kamlesh/WorkSpace/TVH/public/e417daf35b634c1a831f9b4cdccb89c1.htm',
        'crawl_count': 0, 'input': 'https://www.smchealth.org/smmc-find-doctor?page=10',
        'job_id': '16efa636fa3b4782ab57c33b8afbacc2'}
getPage(job)
