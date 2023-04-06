import json
import requests
from settings import YD_TOKEN


uri = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': YD_TOKEN}


def create_folder(folder_name):
    params = {'path': folder_name}
    result = requests.put(uri, headers=headers, params=params)
    return result.status_code


def get_folder_info(folder_name):
    params = {'path': folder_name}
    result = requests.get(uri, headers=headers, params=params)
    if result.status_code == 200:
        res_dict = json.loads(result.text)
        return res_dict.get('type')