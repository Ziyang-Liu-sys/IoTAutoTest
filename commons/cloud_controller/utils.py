import hashlib
import hmac
from datetime import datetime, timezone, timedelta

def get_request_content(request):
    if request.method == "GET":
        return encode_query_params(request.query_params)
    return request.data


def encode_query_params(query_params):
    sorted_q = []
    for key, value in sorted(query_params.items()):
        sorted_q.append(f'{key}={value}')
    return '&'.join(sorted_q).encode('utf-8')


def generate_signature_vpc(access_token: str, encoded_content: bytes, app_key: str):
    app_security = hashlib.md5((access_token + app_key).encode()).hexdigest()
    signature2 = hmac.new(app_security.encode("utf-8"), msg=encoded_content, digestmod='MD5').hexdigest()
    return signature2


def generate_password(s):
    for _ in range(3):
        s = hashlib.md5(s.encode()).hexdigest()
    return s

# 北京时间转时间戳
def beijing_to_timestamp(self,time_str:str, fmt="%Y-%m-%dT%H:%M:%S.%f") -> int:
    # 定义北京时间时区（UTC+8）
    beijing_tz = timezone(timedelta(hours=8))
    
    # 解析输入的时间字符串为 datetime 对象，并加上时区
    dt = datetime.strptime(time_str, fmt).replace(tzinfo=beijing_tz)
        
    # 转为 UTC 时间戳（单位：毫秒）
    return int(dt.timestamp()*1000)
  