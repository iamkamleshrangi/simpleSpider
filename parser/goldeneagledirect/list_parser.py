from bs4 import BeautifulSoup as bs
from lib.mongodb import operations

def parser(job):
    obj = operations()

    file_path = job['storage_path']
    with open(file_path, 'rb') as f:
        content = f.read()
    soup = bs(content, 'html.parser')
    count = 1
    for item in soup.find_all('div',{'class':'list_tile_item'}):
        part_url = item.input.get('onclick')
        part_url = part_url.replace("javascript: location.href='",'')
        part_url = part_url.replace("';",'')
        data = {'part_url' = part_url}
        obj.insert_one('in', 'gold', data)
