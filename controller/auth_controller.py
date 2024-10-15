from model import auth
import datetime
import jwt
from config.config import JWT_ALGORITHM,JWT_SECRET_KEY
from status_code.status import http_statuses

def log_in(*,cursor,email,password):
    response = auth.log_in(cursor=cursor,email=email,password=password)
    print("2",response)
    if response is not None:
        exp_time = datetime.datetime.now()+datetime.timedelta(minutes=15)
        exp_epoc_time = int(str(exp_time.timestamp()).replace('.',''))
        payload = {
            'logInData':response,
            "exp":exp_epoc_time
            
        }
        
        SESSION_TOKEN = jwt.encode(payload,JWT_SECRET_KEY,JWT_ALGORITHM)
        response_code = {
            **http_statuses[200],
            "session":SESSION_TOKEN
        }
        
        return response_code
    else:
       return http_statuses[404]

def sign_up(*,cursor,name,email,password,role = ''):
    response = auth.sign_up(cursor=cursor,name=name,email=email,password=password,role=role)
    if response:
        return http_statuses[200]
    return http_statuses[409]

