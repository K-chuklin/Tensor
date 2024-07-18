import requests
from twoip import TwoIP


def get_ip_location():
    response = requests.get('http://jsonip.com')
    ip = response.json()['ip']
    twoip = TwoIP(key=None)
    data = twoip.geo(ip=ip)
    return data['region_rus']