import requests
import os 
import uuid

def getPage(url):
    html_content = requests.get(url).content
    dir_path = url.split("://")[1].split("/")[0]
    path = savePage(html_content, dir_path)

def savePage(content, save_path):
    dir_path = '../public/%s'%save_path
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = uuid.uuid4().hex + '.htm'
    file_path = dir_path + file_name
    with open(file_path, 'wb') as f:
        f.write(content)
    return file_path 

getPage('http://google.com')
