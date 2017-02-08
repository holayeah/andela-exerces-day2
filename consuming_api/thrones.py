"""
Displays some GOT Characters
"""

import requests

root_url = 'http://anapioficeandfire.com/api'


for page in range(1, 10):
    data = {
        'page': page,
    }
   
    response = requests.get(root_url + '/characters', data)
    data = response.json()

    for character in data:
        if character["aliases"]:
            print(character["aliases"])

