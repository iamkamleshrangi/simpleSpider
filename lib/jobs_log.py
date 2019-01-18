from mongodb import operations
from config_handler import handler

obj = operations()
spot_db = handler('database','spot_db')
spot_col = handler('database', 'spot_col')

def saveJob(job):
    status = obj.insert_one(spot_db, spot_col, job)
    return status

def updateJobStatus(job_id, job):
    status = obj.update_to_mongo(spot_db, spot_col, {'job_id': job_id}, job)
    return status
