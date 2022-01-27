from my_ip_public import http_wrapper
from json import loads


def fetch():
    return http_wrapper.fetch('api.my-ip.io', '/ip')
