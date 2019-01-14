import requests
import os 
import uuid

def getPage(url):
    html_content = requests.get(url).content
    path = savePage(html_content)
    print(path)

def savePage(content):
    dir_path = '../public/'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = uuid.uuid4().hex + '.htm'
    file_path = dir_path + file_name
    with open(file_path, 'wb') as f:
        f.write(content)
    return file_path 
