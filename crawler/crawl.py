import requests
import os 
import uuid
from lib import config_handler

PATH = config_handler('settings', 'public')
def getPage(url):
    html_content = requests.get(url).content
    path = savePage(html_content)

def savePage(content):
    dir_path = PATH 
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = uuid.uuid4().hex + '.htm'
    file_path = dir_path + file_name
    with open(file_path, 'wb') as f:
        f.write(content)
    return file_path 
