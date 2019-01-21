from bs4 import BeautifulSoup as bs


def parser(job):
    file_path = job['storage_path']
    with open(file_path, 'rb') as f:
        content = f.read()
    soup = bs(content, 'html.parser')
    count = 1
    for item in soup.find_all('div',{'class':'list_tile_item'}):
        part_url = item.input.get('onclick')
        part_url = part_url.replace("javascript: location.href='",'')
        part_url = part_url.replace("';",'')
        print(count)
        print(part_url)
        print('*'*50)
        count += 1
