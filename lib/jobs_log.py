from mongodb import operations
from config_handler import handler

obj = operations()
def saveJob(msg):
    spot_db = handler('database','spot_db')
    spot_col = handler('database', 'spot_col')
    status = obj.insert_one(spot_db, spot_col, msg)
    return status
