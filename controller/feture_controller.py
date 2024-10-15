from model.fetures import all_user_data
from status_code.status import http_statuses
def fetch_user(*,cursor,user_id=None):
    response = all_user_data(cursor=cursor,user_id=user_id)
    if response is None:
       return http_statuses[404]
    return{
        **http_statuses[200],
        'data':response
    }