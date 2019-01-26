from bs4 import BeautifulSoup as bs
from lib.mongodb import operations
from lib.common import getContent

def parser(job):
    obj = operations()
    file_path = job['storage_path']
    content = getContent(file_path)
    soup = bs(content, 'html.parser')
    count = 1
    for item in soup.find_all('div',{'class':'list_tile_item'}):
        part_url = item.input.get('onclick')
        part_url = part_url.replace("javascript: location.href='",'')
        part_url = part_url.replace("';",'')
        data = {'part_url' = part_url}
        #obj.insert_one('in', 'gold', data)

job = { "crawl_script" : "crawler.crawl.getPage",
	"job_id" : "19d76fc639614884b8b05337b52853c8",
	"extension" : "htm",
	"is_crawled" : "True",
	"crawl_queue" : "",
	"parse_script" : "parser.goldeneagledirect.parser",
	"priorities" : "high",
	"is_parsed" : "False",
	"storage_id" : "84e68975fedcf16c782695819494bf00",
	"input" : "https://www.goldeneagledirect.com/index.php?pg=15&l=product_list&c=1",
	"job_script" : "jobs.goldeneagledirect.jobs",
	"crawl_count" : 0,
	"parse_queue" : "",
	"storage_path" : "/Users/kamlesh/WorkSpace/TVH/public/d818e1e543ff4c4c88679873178a5e2b.htm"
        }
parser(job)
