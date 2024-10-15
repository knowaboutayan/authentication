import jwt
from jwt import ExpiredSignatureError,InvalidTokenError
from flask import request
from config.config import JWT_ALGORITHM,JWT_SECRET_KEY
import datetime
from status_code.status import http_statuses
from functools import wraps
def check_session(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('DECORATOR')
        x = request.url_rule
        auth_token = request.headers.get('Authorization')
        if auth_token is None:
            return http_statuses[401]
        
        if auth_token.startswith('Bearer '):
            auth_token = auth_token.split()[-1]
        else:
            return http_statuses[403]
        
        try:
            decode_token = jwt.decode(auth_token,JWT_SECRET_KEY,JWT_ALGORITHM)
        except ExpiredSignatureError as err:
            print("!!!ERR!!! decode token",err)
            return http_statuses[419]
        except InvalidTokenError as err:
            return http_statuses[403]
        else:
            session_exp_time = decode_token['exp']
            print(type(session_exp_time))
            if int(session_exp_time) >= int(str(datetime.datetime.utcnow().timestamp()).replace('.','')):
                return func(*args,**kwargs)
            return http_statuses[404]
    return wrapper
