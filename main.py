'''
from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://myshop-bwy316.myinsales.ru/'
LOGIN_ROUTE = 'admin/login/'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 'origin': URL, 'referer': URL + LOGIN_ROUTE}

s = requests.session()

r = s.get(URL)

# t = r.cookies['csrftoken']

login_payload = {
        'login': 'rachik@badalyan.net',
        'password': 'L9HWT9Qh7ecDwUh',
#        'csrfmiddlewaretoken': t
        }

login_req = s.post(URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)

print(login_req)

cookies = login_req.cookies

soup = bs(s.get(URL + 'admin2/discount_codes').text, 'html.parser')
# tbody = soup.find('table', id='table-default table-with-fixed-headers')

print(soup.prettify())

def login(mail, password):
        s = requests.session
        payload = {
                'email' = rachik@badalyan.net,
                'password' = L9HWT9Qh7ecDwUh
        }
        res = s.post('https://myshop-bwy316.myinsales.ru/admin/login', data = payload)
        s.headers.update({})
'''
'''
from bs4 import BeautifulSoup as bs
import requests

#This URL will be the URL that your login form points to with the "action" tag.
URL = 'https://myshop-bwy316.myinsales.ru/admin/login'

#This URL is the page you actually want to pull down with requests.
ENDPOINT = 'https://myshop-bwy316.myinsales.ru/admin2/discount_codes'

payload = {
    'username': 'rachik@badalyan.net',
    'pass': 'L9HWT9Qh7ecDwUh'
}

with requests.Session() as session:
    post = session.post(URL, data=payload)
    r = session.get(ENDPOINT)
    print(r.text)   #or whatever else you want to do with the request data!
'''

from bs4 import BeautifulSoup as bs
import requests

import requests

cookies = {
    'carrotquest_device_guid': '7d5b7409-983b-46c4-b87d-918f164703e5',
    'carrotquest_uid': '1255428562748441450',
    'carrotquest_auth_token': 'user.1255428562748441450.9319-22a7b9d19c8c648c68dcc81b759.37339ecf1f1a90d601f1c5ff8872687e733023e46a307001',
    'first_current_location': '%2Forders%2Fsuccessful%3Fid%3D286dd6430d98758ebf0a6b02d179db5b',
    'first_referer': 'https%3A%2F%2Fmyshop-bwy316.myinsales.ru%2Fadmin2%2Forders%2F62692119',
    'referer': 'https%3A%2F%2Fmyshop-bwy316.myinsales.ru%2Fadmin2%2Forders%2F62692119',
    'current_location': '%2Forders%2Fsuccessful%3Fid%3D286dd6430d98758ebf0a6b02d179db5b',
    'carrotquest_realtime_services_transport': 'wss',
    'cart': 'json',
    'ins_order_version': '1666347803.1326976',
    'carrotquest_hide_all_unread_popups': 'true',
    'carrotquest_hide_all_unread_popups': 'true',
    'carrotquest_hide_all_unread_popups': 'true',
    'authorized_domains': 'e30%3D%0A',
    'ins_myshop-bwy316': '4f6d171332d861753db2b97213677bff',
    'carrotquest_session': 'tepjg05gpx1b0i0x7cuseq26isbb60x1',
    'carrotquest_session_started': '1',
}

headers = {
    'authority': 'myshop-bwy316.myinsales.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'carrotquest_device_guid=7d5b7409-983b-46c4-b87d-918f164703e5; carrotquest_uid=1255428562748441450; carrotquest_auth_token=user.1255428562748441450.9319-22a7b9d19c8c648c68dcc81b759.37339ecf1f1a90d601f1c5ff8872687e733023e46a307001; first_current_location=%2Forders%2Fsuccessful%3Fid%3D286dd6430d98758ebf0a6b02d179db5b; first_referer=https%3A%2F%2Fmyshop-bwy316.myinsales.ru%2Fadmin2%2Forders%2F62692119; referer=https%3A%2F%2Fmyshop-bwy316.myinsales.ru%2Fadmin2%2Forders%2F62692119; current_location=%2Forders%2Fsuccessful%3Fid%3D286dd6430d98758ebf0a6b02d179db5b; carrotquest_realtime_services_transport=wss; cart=json; ins_order_version=1666347803.1326976; carrotquest_hide_all_unread_popups=true; carrotquest_hide_all_unread_popups=true; carrotquest_hide_all_unread_popups=true; authorized_domains=e30%3D%0A; ins_myshop-bwy316=4f6d171332d861753db2b97213677bff; carrotquest_session=tepjg05gpx1b0i0x7cuseq26isbb60x1; carrotquest_session_started=1',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

response = requests.get('https://myshop-bwy316.myinsales.ru/admin/login', cookies=cookies, headers=headers)

soup = bs(response.content, 'html.parser')

print(soup.prettify)
