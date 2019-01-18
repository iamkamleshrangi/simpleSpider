import hashlib
import uuid

def getId(content):
   content_id = hashlib.md5(content.encode())
   return content_id.hexdigest()

def getguId():
    guid = uuid.uuid4().hex
    return guid
