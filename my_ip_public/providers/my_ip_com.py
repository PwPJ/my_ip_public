from my_ip_public import http_wrapper
from json import loads


def fetch():
    status, result = http_wrapper.fetch('api.myip.com', '/')
    if status:
        result = loads(result)['ip']
    return status, result
