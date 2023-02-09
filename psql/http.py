import requests
import json
from requests.exceptions import HTTPError
import ssl
import my_insert as lri

ssl._create_default_https_context = ssl._create_unverified_context

# Global env
sand_host = "http://"
test_host = "http://"
role = 'role='
headers = {'accept': '*/*'}
get_token = 'endpoint/endpoint/endpoint'
post_license = 'another_endpoint/another_endpoint'
# Локальные переменные для заявлений
file_ = 'path/to/files'
inn = '2048302930'
somethingParametr = input("Enter your's somethingParametr\n")
anotherYetParametr = input("Enter your's anotherYetParametr\n")
# Краткое название организации
orgParametr = 'Stoic'
# Полное название организации
orgFullParametr = 'Stoic_01'

# Автоматическое получение токена
try:
    response = requests.get(f"{sand_host}{get_token}?{role}", headers = headers)
    response.raise_for_status()
except HTTPError as http_err:
    print(f"HTTP error occured: {http_err}")
except Exception as err:
    print(f"Other error occured: {err}")
else:
    token = response.text
    headers['Authorization'] = token

# Список кодов
php_test = [1, 5, 6, 11, 22]
t_test = [15, 16, 17]

# Отправка одного запроса

def single_post():
    files = {
        'file': open(file_, 'rb'),
        'inn': inn,
        'somethingParametr': somethingParametr,
        'orgParametr': orgParametr,
        'orgFullParametr': orgFullParametr,
        'anotherYetParametr': anotherYetParametr
            }
    try:
        response = requests.post(f'{host}{post_license}', headers=headers, files=files)
        response.raise_for_status()
        response.encoding = 'utf-8'
    except HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except Exception as err:
        print(f"Other error occured: {err}")
    else:
        textum = response.text
        dict_request = json.loads(textum)
        print(dict_request['requestId'])
        return dict_request['requestId']

# POST-запрос нескольких запросов.

def many_post():
    for index in php_test:
        files = {
            'file': open(file_, 'rb'),
            'inn': inn,
            'somethingParametr': str(index),
            'orgParametr': orgParametr,
            'orgFullParametr': orgFullParametr,
            'anotherYetParametr': anotherYetParametr
                }
        try:
            response = requests.post(f'{host}{post_license}', headers=headers, files=files)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP error occured: {http_err}")
        except Exception as err:
            print(f"Other error occured: {err}")
        else:
            textum = response.text
            dict_request = json.loads(textum)
            print(dict_request['requestId'])

if somethingParametr:
    request_id = single_post()
    lri.connect_to_insert(request_id)
else:
    many_post()
