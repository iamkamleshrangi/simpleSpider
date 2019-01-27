from bs4 import BeautifulSoup as bs
from lib.common import getContent
from lib.mongodb import operations
from lib.jobs_log import updateJobStatus

def parser(job):
    obj = operations()
    file_path = job['storage_path']
    content = getContent(file_path)
    soup = bs(content, 'html.parser')
    for item in soup.find_all('div',{'class':'list_tile_item'}):
        part_url = item.input.get('onclick')
        part_url = part_url.replace("javascript: location.href='",'')
        part_url = part_url.replace("';",'')
        data = {'part_url' : part_url,
                'job_id': job['job_id']
                }
        obj.insert_one('in', 'gold', data)
    obj.closeConnection()
    job['is_parsed'] = "True"
    updateJobStatus(job['job_id'], job)

job = {'is_crawled': 'True', 'is_parsed': 'False', 'storage_id': '7c5423c27dd1791a211221e9f6af0334', 'extension': 'htm',
        'crawl_queue': '', 'parse_queue': '', 'job_script': 'jobs.goldeneagledirect.jobs',
        'crawl_script': 'crawler.crawl.getPage', 
        'parse_script': 'parser.goldeneagledirect.list_parser.parser', 
        'priorities': 'high', 
        'storage_path': '/Users/kamlesh/WorkSpace/TVH/public/d5fa6c9baf8c450ba50c6430d4b00179.htm',
        'crawl_count': 0, 'input': 'https://www.goldeneagledirect.com/index.php?pg=43&l=product_list&c=1', 
        'job_id': 'ec364e285d1d40d8b9f5c149ef61841e'}

parser(job)

