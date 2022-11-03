import requests
from bs4 import BeautifulSoup as Bs

url = 'https://www.reddit.com/login'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

payload = {
    'csrf_token': '',
    'otp': '',
    'password': '',
    'dest': '',
    'username': ''
}

session = requests.Session()
response = session.get(url, headers=headers)
session.headers.update()
soap = Bs(response.text, 'lxml')
inputs = soap.find('form', id='globals').find_all('input')
csrf_token = inputs[1].get('value')
payload['csrf_token'] = csrf_token
payload['username'] = input('username: ')
payload['password'] = input('password: ')
response = session.post(url, headers=headers, data=payload)
session.headers.update()
if response.json().get('details') != None:
    otp = int(input('otp: '))
    payload['otp'] = otp
    response = session.post(url, headers=headers, data=payload)
    session.headers.update()
print(response.json())

#Continue your session here
