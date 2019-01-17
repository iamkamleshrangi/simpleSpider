import requests
import os 
import uuid
from lib.config_handler import handler

PATH = handler('settings','public_path')
def getPage(url):
    html_content = requests.get(url).content
    file_path = savePage(html_content)
    return file_path

def savePage(content):
    dir_path = PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = uuid.uuid4().hex + '.htm'
    file_path = dir_path + file_name
    with open(file_path, 'wb') as f:
        f.write(content)
    return file_path 
